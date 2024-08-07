import uuid
from decimal import Decimal, InvalidOperation

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from airbnb_properties.models import Property
from user_profile.models import UserProfile


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=False, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    guest_count = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False,
                                  blank=False, default='')

    def _generate_order_number(self):
        """ Generate random unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total')
        )['lineitem_total__sum'] or 0
        self.grand_total = self.order_total
        self.save()

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
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    property = models.ForeignKey(Property, null=False, blank=False,
                                 on_delete=models.CASCADE)
    date_range = models.CharField(max_length=255, null=True)
    total_days = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
    taxi_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     null=False, blank=False, default=0.00)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        try:
            # Ensure price_per_night is a Decimal
            price_per_night = self.property.price_per_night
            print("this is price per night (type):", price_per_night,
                  type(price_per_night))
            if not isinstance(price_per_night, Decimal):
                price_per_night = Decimal(price_per_night)

            # Make sure that total_days is converted to Decimal
            total_days = Decimal(self.total_days)

            # Ensure taxi_price is a Decimal
            taxi_price = Decimal(self.taxi_price)

            # Calculate lineitem_total including taxi_price
            self.lineitem_total = (price_per_night * total_days) + taxi_price
        except InvalidOperation as e:
            # Log or handle the error as appropriate
            raise ValueError(f"Invalid operation for Decimal conversion: {e}")

        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'Property Name {self.property.name} \
                 on order {self.order.order_number}'
