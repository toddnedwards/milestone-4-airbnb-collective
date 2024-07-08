from django.urls import path
from . import views

urlpatterns = [
    path('', views.airbnb_properties, name='properties'),
    path('<str:property_id>/', views.property_details, name='property_details'),
]