from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Property(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  
    location = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True)
    description = models.TextField()
    full_description = models.TextField(null=True, blank=True)
    price_per_night = models.IntegerField(max_length=10, null=True, blank=True)
    availability = models.CharField(max_length=50, null=True, blank=True)
    distance_to_airport = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    has_wifi = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    non_smoking = models.BooleanField(default=False)
    pet_friendly = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)
    image_kitchen = models.ImageField(null=True, blank=True)
    image_bathroom = models.ImageField(null=True, blank=True)
    total_days = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "properties"
        

class Date(models.Model):

    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    date_range = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name