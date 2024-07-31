from django.contrib import admin
from .models import Property, Category

# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'location',
        'description',
        'price_per_night',
        'availability',
        'image',
        'image_kitchen',
        'image_bathroom',
        'distance_to_airport',
        'bedrooms'
    )

admin.site.register(Property, PropertyAdmin)
admin.site.register(Category)