from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from airbnb_properties.models import Property


def cart_contents(request):

    cart_items = []
    total_days = 0
    property_count = 0
    grand_total = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        property = get_object_or_404(Property, pk=item_id)
        if 'date_ranges' in item_data:
            for date_range in item_data['date_ranges']:
                start_date_str, end_date_str = date_range.split(' - ')
                start_date = datetime.strptime(start_date_str, '%d %b %Y')
                end_date = datetime.strptime(end_date_str, '%d %b %Y')
                days = (end_date - start_date).days
                total_days += days
                property_count += 1


                taxi_price = property.distance_to_airport * 3
                property_total = (total_days * property.price_per_night) + taxi_price

                grand_total += property_total
                cart_items.append({
                    'item_id': item_id,
                    'date_range': date_range,
                    'days': days,
                    'property': property,
                    'property_total': property_total,
                    'taxi_price': taxi_price,
                    'grand_total': grand_total,
                })

    context = {
        'cart_items': cart_items,
        'total_days': total_days,
        'property_count': property_count,
        'grand_total': grand_total,
    }

    return context