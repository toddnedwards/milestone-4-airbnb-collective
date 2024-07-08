from django.urls import path
from . import views

urlpatterns = [
    path('', views.airbnb_properties, name='properties'),
    path('<str:property_id>/', views.property_details, name='property_details'),
    path('delete_property/<str:property_id>/', views.delete_property, name='delete_property'),
    path('edit_property/<str:property_id>/', views.edit_property, name='edit_property'),
]