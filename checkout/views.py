from django.shortcuts import render, get_object_or_404
from .models import Booking, Property

# Create your views here.
def book_property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)

    context = {
        'booked_dates': booked_dates,
    }

    return render(request, 'properties/checkout.html', context)