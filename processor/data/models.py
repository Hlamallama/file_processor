import typing
from django.db import models

class FileData(models.Model):
    date = models.DateTimeField()
    country = models.CharField(max_length=200)
    purchase = models.FloatField()
    currency = models.CharField(max_length=200)
    net = models.FloatField()
    Vat = models.IntegerField()


class Country(models.Model):
    id = models.DateTimeField()
    currency = models.CharField(max_length=200)
    name = models.FloatField()