from django.urls import path
from . import views

urlpatterns = [
    path('', views.airbnb_properties, name='properties')
]