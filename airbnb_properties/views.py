from django.shortcuts import render
from .models import Property

# Create your views here.

def airbnb_properties(request):
    """ A view to show all properties that exist in properties DB """

    properties = Property.objects.all()

    context = {
        'properties': properties,
    }


    return render(request, 'properties/index.html', context)
