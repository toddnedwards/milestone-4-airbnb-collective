from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, "cart.html", {})

def cart_add(request, property_id):
    total_days = int(request.POST.get('total_days'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})


def cart_delete(request):
    pass

def cart_update(request):
    pass