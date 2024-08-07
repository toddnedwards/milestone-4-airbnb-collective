from django.db import models

# Create your models here.


class Faq(models.Model):

    answer = models.CharField(max_length=254)
    question = models.CharField(max_length=254)

    def __str__(self):
        return self.question
