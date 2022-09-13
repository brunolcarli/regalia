from django.db import models


class HouseOffer(models.Model):
    price = models.FloatField()
    url = models.TextField()
    description = models.TextField()
    category = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    condominium = models.FloatField(null=True)
    property_tax = models.FloatField(null=True)  # IPTU
    useful_area = models.CharField(max_length=50, null=True)
    bedrooms = models.IntegerField(null=True)
    bathrooms = models.IntegerField(null=True)
    parking_spaces = models.IntegerField(null=True)
    postal_code = models.CharField(max_length=100, null=True)  # CEP
    county = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    date_reference = models.DateField(auto_now_add=True, null=True)
