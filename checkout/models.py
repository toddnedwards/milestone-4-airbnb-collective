import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from airbnb_properties.models import Property

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=True)
    county = models.CharField(max_length=80, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ Generate random unique order number using UUID """
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """ 
        Override original save method to set the 
        order number if it hasn't been set already 
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    property = models.ForeignKey(Property, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.property.price * self.property.total_days
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Property Name {self.property.name} on order {self.order.order_number}'