from django.urls import path
from . import views
from .views import booked_dates
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('booked_dates/<property_id>/', booked_dates, name='booked_dates'),
]
