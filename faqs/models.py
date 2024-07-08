from django.db import models

# Create your models here.
class Faqs(models.Model):

    answers = models.CharField(max_length=254)
    questions = models.CharField(max_length=254)



    def __str__(self):
        return self.name