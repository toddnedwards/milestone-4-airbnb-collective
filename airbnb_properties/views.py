from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Property

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


@login_required
def edit_property(request, property_id):
    """ Edit property details """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to see this page.')
        return redirect(reverse('home'))

    property = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property details have been successfully edited')
            return redirect(reverse('property_details', args=[property_id]))
        else:
            form = PropertyForm(instance=property)
            messages.info(request, f'You are editing {property.name}- {property.location}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product, 
    }

    return render(request, template, context)

@login_required
def delete_property(request, property_id):
    """ Delete property from the properties list """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission to see this page.')
        return redirect(reverse('home'))

    property = get_object_or_404(Property, pk=property_id)
    property.delete()
    messages.success(request, 'Property Deleted')
    return redirect(reverse('home'))
