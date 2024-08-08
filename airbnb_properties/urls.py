from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.airbnb_properties, name='properties'),
    path('add/', views.add_property, name='add_property'),
    path('<int:property_id>/', views.property_details, name='property_details'),
    path('edit/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete/<int:property_id>/', views.delete_property, name='delete_property'),
]
