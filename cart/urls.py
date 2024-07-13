from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add/<item_id>', views.cart_add, name='cart_add'),
    path('delete/<item_id>', views.cart_delete, name='cart_delete'),
    path('update/<item_id>', views.cart_update, name='cart_update'),
]