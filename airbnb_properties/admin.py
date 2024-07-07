from django.contrib import admin
from .models import Property

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'location',
        'description',
        'price_per_night',
        'availability',
        'image',
        'distance_to_airport',
        'bedrooms'
    )

admin.site.register(Property, PropertyAdmin)