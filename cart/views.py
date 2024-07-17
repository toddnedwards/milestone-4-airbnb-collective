from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from airbnb_properties.models import Property

# Create your views here.
def cart(request):
    return render(request, "cart.html")


def cart_add(request, item_id):

    property = get_object_or_404(Property, pk=item_id)
    total_days = int(request.POST.get('total_days'))
    date_range = request.POST.get('date_range')

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id not in cart:
        cart[item_id] = {'total_days': total_days, 'date_ranges': [date_range]}
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(reverse('cart'))

def remove_from_cart(request, item_id):
    """Remove property from cart"""

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        messages.success(request, 'Property removed from cart successfully')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


def cart_update(request):
    pass


def add_taxi(request):
            return redirect(reverse('cart'))
