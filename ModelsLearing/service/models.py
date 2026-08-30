from django.db import models

# Create your models here.

class Service(models.Model):
    name =models.CharField( max_length=50)
    discreption =models.TextField(max_length=1000)
    salary = models.IntegerField()

class FavYoutuber(models.Model):
    name = models.CharField(max_length=100)
    subcribers = models.IntegerField()
    