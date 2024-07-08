from django.shortcuts import render, get_object_or_404
from .models import Property
Property.objects.all().delete()

# Create your views here.

def airbnb_properties(request):
    """ A view to show all properties that exist in properties DB """

    properties = Property.objects.all()

    context = {
        'properties': properties,
    }

    return render(request, 'properties/index.html', context)


def property_details(request, property_id):
    """ A view to show an individual page for each property to find out more information and to book selected property"""

    property = get_object_or_404(Property, pk=property_id)

    context = {
        'property': property,
    }

    return render(request, 'properties/property_details.html', context)
