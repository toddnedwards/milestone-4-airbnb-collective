from django.shortcuts import render


# Create your views here.

def airbnb_properties(request):

    return render(request, 'properties/index.html')