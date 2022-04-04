from django.db import models


# Create your models here.
class GasPrice(models.Model):
    gas_station_name = models.CharField(max_length=50)
    datetime_reference = models.DateTimeField(auto_now_add=True)
    gas_price = models.FloatField()
