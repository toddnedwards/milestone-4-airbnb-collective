from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<int:property_id>/', views.book_property, name='checkout'),
]