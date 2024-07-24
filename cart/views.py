from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from datetime import datetime

from airbnb_properties.models import Property


# Create your views here.
def cart(request):
    return render(request, "cart/cart.html")


def cart_add(request, item_id):

    print(request.POST)
    property = get_object_or_404(Property, pk=item_id)
    date_range = request.POST.get('date_range')
    start_date_str, end_date_str = date_range.split(' - ')
    start_date = datetime.strptime(start_date_str, '%d %b %Y')
    end_date = datetime.strptime(end_date_str, '%d %b %Y')
    total_days = (end_date - start_date).days
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in cart:
        cart[item_id] = {'total_days': total_days, 'date_ranges': [date_range]}
    else:
        cart[item_id]['total_days'] = total_days
        cart[item_id]['date_ranges'].append(date_range)
    
    request.session['cart'] = cart
    print(request.session['cart'])
    messages.success(request, 'Property added to cart successfully')
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """Remove property from cart"""

    try:
        cart = request.session.get('cart', {})
        if item_id in cart:
                cart.pop(item_id)
                messages.success(request, 'Property removed from cart successfully')
        else:
            messages.warning(request, 'Property not found in cart')

        request.session['cart'] = cart
        return redirect('cart')

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def cart_update(request):
    
        return redirect(reverse('property_details'))


def add_taxi(request, item_id):
    property = get_object_or_404(Property, pk=item_id)
    taxi_price = property.distance_to_airport * 3
    cart = request.session.get('cart', {})

    if item_id in cart:
        cart[item_id]['add_taxi'] = taxi_price
    else:
        cart[item_id] = {'add_taxi': taxi_price}
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_taxi(request, item_id):
    cart = request.session.get('cart', {})

    if item_id in cart and 'add_taxi' in cart[item_id]:
        del cart[item_id]['add_taxi']

        if not cart[item_id]:
            del cart[item_id]
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))