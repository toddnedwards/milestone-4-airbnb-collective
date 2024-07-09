import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from airbnb_properties.models import Property

from django_countries.fields import CountryField


# Create your models here.
class Booking(models.Model):   
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
