from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem


from airbnb_properties.models import Property
from user_profile.models import UserProfile
from user_profile.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json
from datetime import datetime, timedelta


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request, 'Sorry, your payment cannot be processed right now.'
                     'Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            current_cart = cart_contents(request)
            total_days = current_cart['total_days']
            order.grand_total = current_cart['grand_total']
            order.total_days = total_days
            order.stripe_pid = request.POST.get(
                'client_secret').split('_secret')[0]
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    property = Property.objects.get(id=item_id)
                    taxi_price = property.distance_to_airport * 3
                    if isinstance(item_data, dict) and 'date_ranges' in item_data:
                        for date_range in item_data['date_ranges']:
                            start_date_str, end_date_str = date_range.split(
                                                           ' - ')
                            start_date = datetime.strptime(start_date_str,
                                                           '%d %b %Y').date()
                            end_date = datetime.strptime(
                                       end_date_str, '%d %b %Y').date()
                            days = (end_date - start_date).days
                            sub_total = days * property.price_per_night
                            lineitem_total = sub_total + taxi_price
                            order_line_item = OrderLineItem(
                                order=order,
                                property=property,
                                date_range=date_range,
                                start_date=start_date,
                                end_date=end_date,
                                total_days=int(days),
                                taxi_price=taxi_price,
                                sub_total=sub_total,
                                lineitem_total=lineitem_total,
                            )
                            order_line_item.save()
                except ValueError as e:
                    # Log or handle the error if date_range format is invalid
                    print(f"Date range format error: {e}")
                except Property.DoesNotExist:
                    messages.error(
                        request, ("One of the properties in your cart "
                                  "wasn't found in our database. "
                                  "Please call us for assistance!"))
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request, 'There was an error with your form. '
                         'Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request, "There's nothing in your cart at the moment")
            return redirect(reverse('properties'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, 'checkout/checkout.html', context)


def booked_dates(request, property_id):
    booked_dates = OrderLineItem.objects.filter(
            property_id=property_id).values_list('date_range', flat=True)

    excluded_dates = []
    for date_range in booked_dates:
        if date_range:
            start_date_str, end_date_str = date_range.split(' - ')
            start_date = datetime.strptime(start_date_str, '%d %b %Y')
            end_date = datetime.strptime(end_date_str, '%d %b %Y')
            while start_date <= end_date:
                excluded_dates.append(
                    start_date.strftime('%Y-%m-%d'))
                start_date += timedelta(days=1)

    return JsonResponse({'excluded_dates': excluded_dates})


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request, f'Order successfully processed! '
        'Your order number is {order_number}.'
        'A confirmation email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_line_items': order.lineitems.all(),
    }

    return render(request, template, context)
