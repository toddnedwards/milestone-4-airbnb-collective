from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "you have nothing in cart at the moment")
        return redirect(reverse('properties'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PdZpJFZHmSDqVxQZj4THNgKhCgZvccY7ktOjLbzsCFYVD6IxAFVCmhxB3xYNXeR3wdQHUZxXoryX8QODUo7QbKx00j4EUMAEp',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
