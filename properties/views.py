from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('/properties', views.properties, name='properties'),
]