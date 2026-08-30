from django.db import models
from tinymce.models import HTMLField 

# Create your models here.

class Service(models.Model):
    name =models.CharField( max_length=50)
    discreption =HTMLField()
    salary = models.IntegerField()

class FavYoutuber(models.Model):
    name = models.CharField(max_length=100)
    subcribers = models.IntegerField()
    