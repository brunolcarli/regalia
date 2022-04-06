from django.db import models


# Create your models here.
class GasPrice(models.Model):
    region = models.CharField(max_length=50, null=True)
    datetime_reference = models.DateField(auto_now_add=True, null=True)
    gas_price = models.FloatField(null=True)
    gas_lower_price = models.FloatField(null=True)
    gas_higher_price = models.FloatField(null=True)
    ethanol_price = models.FloatField(null=True)
    ethanol_lower_price = models.FloatField(null=True)
    ethanol_higher_price = models.FloatField(null=True)
