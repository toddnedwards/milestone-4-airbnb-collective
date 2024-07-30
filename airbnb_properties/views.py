from datetime import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .models import Property, Date
from .forms import PropertyForm, DateForm

# Create your views here.

def airbnb_properties(request):
    """ A view to show all properties that exist in properties DB """

    properties = Property.objects.all()
    query = None
    no_results = False
    filtered = False
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                properties = properties.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            properties = properties.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('properties'))

            queries = Q(name__icontains=query) | Q(location__icontains=query)
            filtered_properties = properties.filter(queries)
            if not filtered_properties.exists():
                no_results = True
            else:
                messages.error(request, "No results for your search. Please try again")
                properties = filtered_properties
                filtered = True

    current_sorting = f'{sort}_{direction}'    

    context = {
        'properties': properties,
        'search_term': query,
        'no_results': no_results,
        'filtered': filtered,
        'current_sorting': current_sorting,
    }

    return render(request, 'properties/properties.html', context)


def property_details(request, property_id):
    """ A view to show an individual page for each property to find out more
        information and to book selected property"""

    property = get_object_or_404(Property, pk=property_id)
    date_range = request.GET.get('date_range', '')

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.save(commit=False)
            date.property = property
            start_date_str, end_date_str = date.date_range.split(' - ')
            date.start_date = datetime.strptime(start_date_str, '%d %b %Y')
            date.end_date = datetime.strptime(end_date_str, '%d %b %Y')
            date.save()

            if 'cart' not in request.session:
                request.session['cart'] = {}
            request.session['cart'][property_id] = {
                'date_ranges': [date.date_range],
                'property_details': {
                    'name': property.name,
                    'location': property.location,
                },
            }

            request.session.modified = True
            return redirect('cart')

    else:
        form = DateForm(initial={'date_range': date_range})

    context = {
        'property': property,
        'form': form,
        'date_range': date_range,
    }

    return render(request, 'properties/property_details.html', context)

def datepicker_view(request):
    if request.method == 'POST':
        date_range = request.POST.get('date_range')


@login_required
def edit_property(request, property_id):
    """ Edit property details """
    if not request.user.is_superuser:
        messages.error.request(request, 'You do not have permission to see this page.')
        return redirect(reverse('home'))

    property = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            messages.success(request, 'Property details have been successfully edited')
            return redirect(reverse('property_details', args=[property.id]))
        else:
            messages.error(request, 'Failed to update property. Please ensure the form is valid.')
    else:
        form = PropertyForm(instance=property)
        messages.info(request, f'You are editing {property.name}')

    template = 'properties/edit_property.html'
    context = {
        'form': form,
        'property': property, 
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