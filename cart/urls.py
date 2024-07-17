from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>/', views.cart_add, name='cart_add'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<item_id>/', views.cart_update, name='cart_update'),
    path('add_taxi/', views.add_taxi, name='add_taxi'),
]
 