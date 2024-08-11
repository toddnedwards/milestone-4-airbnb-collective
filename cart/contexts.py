from decimal import Decimal
from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404
from airbnb_properties.models import Property


def cart_contents(request):

    cart = request.session.get('cart', {})
    cart_items = []
    total_days = 0
    property_count = 0
    property_total = Decimal('0.00')
    taxi_quote = Decimal('0.00')
    grand_total = Decimal('0.00')
    discount_amount = Decimal('0.00')

    for item_id, item_data in cart.items():
        property = get_object_or_404(Property, pk=item_id)
        taxi_price = item_data.get('add_taxi', Decimal('0.00'))
        guest_count = item_data.get('guest_count')
        if 'date_ranges' in item_data:
            for date_range in item_data['date_ranges']:
                try:
                    start_date_str, end_date_str = date_range.split(' - ')
                    start_date = datetime.strptime(start_date_str, '%d %b %Y')
                    end_date = datetime.strptime(end_date_str, '%d %b %Y')
                    days = (end_date - start_date).days
                    total_days += days
                    property_count += 1
                    original_property_total = days * property.price_per_night

                    if total_days > settings.TOTAL_DAYS_DISCOUNT_THRESHOLD:
                        discount_amount = original_property_total * Decimal('0.1')
                        property_total = original_property_total - discount_amount
                    else:
                        property_total = days * property.price_per_night
                             
                    taxi_quote = property.distance_to_airport * Decimal('3')
                    sub_total = property_total + taxi_price

                    grand_total += sub_total

                    cart_items.append({
                        'item_id': item_id,
                        'date_range': date_range,
                        'days': days,
                        'property': property,
                        'property_total': property_total,
                        'total_days': total_days,
                        'sub_total': sub_total,
                        'taxi_price': taxi_price,
                        'guest_count': guest_count,
                        'discount_amount': discount_amount,
                    })

                except ValueError:
                    pass

    if total_days < settings.TOTAL_DAYS_DISCOUNT_THRESHOLD:
        discount_delta = settings.TOTAL_DAYS_DISCOUNT_THRESHOLD - total_days
    else:
        discount_delta = 0

    context = {
        'cart_items': cart_items,
        'total_days': total_days,
        'property_count': property_count,
        'property_total': property_total,
        'total_days': total_days,
        'grand_total': grand_total,
        'taxi_quote': taxi_quote,
        'discount_threshold': settings.TOTAL_DAYS_DISCOUNT_THRESHOLD,
        'discount_amount': discount_amount,
        'discount_delta': discount_delta,
    }

    return context
