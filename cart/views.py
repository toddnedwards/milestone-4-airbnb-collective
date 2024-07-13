from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

from airbnb_properties.models import Property

# Create your views here.
def cart(request):
    return render(request, "cart.html", {})


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


def cart_delete(request, item_id):
    cart = request.session.get('cart', {})
    if item_id in cart:
        del cart[item_id]

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def cart_update(request):
    pass