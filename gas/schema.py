import graphene
from gas.models import GasPrice


class GasPriceType(graphene.ObjectType):
    gas_station_name = graphene.String()
    gas_price = graphene.Float()
    datetime_reference = graphene.DateTime()


class Query(graphene.ObjectType):
    gas_prices = graphene.List(GasPriceType)

    def resolve_gas_prices(self, info, **kwargs):
        return GasPrice.objects.filter(**kwargs)
