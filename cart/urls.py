from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>/', views.cart_add, name='cart_add'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<property_id>/', views.cart_update, name='cart_update'),
    path('add_taxi/<str:item_id>/', views.add_taxi, name='add_taxi'),
    path('remove_taxi/<str:item_id>/', views.remove_taxi, name='remove_taxi'),
]
 