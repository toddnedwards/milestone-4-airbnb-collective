from django.db import models

class Contact(models.Model):

    email = models.EmailField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=255, null=False, blank=False)