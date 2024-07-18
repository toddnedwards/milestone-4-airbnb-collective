from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from airbnb_properties.models import Property
from cart.contexts import cart_contents

import stripe
import datetime

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            print("form is valid")
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    property = get_object_or_404(Property, pk=item_id)
                    if isinstance(item_data, int):
                        date_range = item_data
                        start_date_str, end_date_str = date_range.split(' - ')
                        start_date = datetime.datetime.strptime(start_date_str, '%d %b %Y')
                        end_date = datetime.datetime.strptime(end_date_str, '%d %b %Y')
                        total_days = (end_date - start_date).days
                        property_count += 1

                        taxi_price = property.distance_to_airport * 3
                        property_total = (total_days * property.price_per_night) + taxi_price
                        cart_items.append({
                            'item_id': item_id,
                            'date_range': date_range,
                            'days': days,
                            'property': property,
                            'property_total': property_total,
                            'taxi_price': taxi_price,
                            'grand_total': grand_total,
                        })
                except Property.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print("form not valid")
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "You have nothing in your cart at the moment.")
            return redirect(reverse('properties'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation  \
            email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)