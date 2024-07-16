from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.airbnb_properties, name='properties'),
    path('<property_id>/', views.property_details, name='property_details'),
    path('edit/<str:property_id>/', views.edit_property, name='edit_property'),
    path('delete/<property_id>/', views.delete_property, name='delete_property'),
]