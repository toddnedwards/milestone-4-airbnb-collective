from django.shortcuts import render, get_object_or_404

from .models import BookingOrder, PersonalDetails

# Create your views here.
def checkout(request):

    if request.method == 'POST':
        

    return render(request, 'checkout/checkout.html')