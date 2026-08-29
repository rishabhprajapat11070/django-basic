from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    title = models.TextField(max_length=1000)
