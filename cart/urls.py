from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<property_id>/', views.cart_add, name='cart_add'),
    path('delete/<property_id>/', views.cart_delete, name='cart_delete'),
    path('update/<property_id>/', views.cart_update, name='cart_update'),
]