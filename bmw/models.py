from django.db import models


class BMWOffer(models.Model):
    price = models.FloatField()
    url = models.TextField()
    car_model = models.CharField(max_length=100, null=True)
    car_year = models.IntegerField()
    km = models.IntegerField(null=True)
    power = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=50, null=True)
    seller_name = models.CharField(max_length=250, null=True)
