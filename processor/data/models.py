
from django.db import models

class FileData(models.Model):
    date = models.CharField(max_length=9)
    country = models.CharField(max_length=2)
    purchase = models.FloatField()
    currency = models.CharField(max_length=3)
    net = models.FloatField()
    Vat = models.FloatField()