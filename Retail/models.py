from django.db import models
from Retail.models import Listing

# Create your models here.
class Products(models.Model):
    Serial_no = models.CharField(unique=True, max_length=16)
    Name = models.CharField(max_length=100)
    Metric = models.CharField(max_length=20, null=True)
    Items_available = Items


class Listing(models.Model):
    Serial_no = models.ForeignKey(Products, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Metric = models.CharField(max_length=20, null=True)


Items = Listing.objects.filter(Serial_no)
