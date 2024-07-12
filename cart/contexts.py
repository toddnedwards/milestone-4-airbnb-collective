from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from airbnb_properties.models import Property


def cart_contents(request):

    cart_items = []
    total_days = 0
    property_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        property = get_object_or_404(Property, pk=item_id)
        for date_range in item_data['date_ranges']:
            start_date_str, end_date = date_range.split(' - ')
            start_date = datetime.strptime(start_date_str, '%d %b %Y')
            end_date = datetime.strptime(end_date_str, '%d %b %Y')
            days = (end_date - start_date).days
            total_days += days
            property_count += 1
            cart_items.append({
                'item_id': item_id,
                'date_range': date_range,
                'days': days,
                'property': property
            })

    context = {
        'cart_items': cart_items,
        'total_days': total_days,
        'property_count': property_count
    }

    return context