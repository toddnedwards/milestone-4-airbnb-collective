from django.db import models

# Create your models here.
class Property(models.Model):

    id = models.CharField(max_length=254, primary_key=True)
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    full_description = models.TextField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.CharField(max_length=50, null=True, blank=True)
    distance_to_airport = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    has_wifi = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    non_smoking = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name

class Date(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    date_range = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()