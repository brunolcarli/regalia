import graphene
from gas.models import GasPrice


class GasPriceType(graphene.ObjectType):
    region = graphene.String(description='City region of reference')
    gasoline_average_price = graphene.Float(
        description='Gasoline average price for the region in the last 15 days'
    )
    gasoline_lowest_price = graphene.Float(
        description='Gasoline lowest price for the region in the last 15 days'
    )
    gasoline_highest_price = graphene.Float(
        description='Gasoline highest price for the region in the last 15 days'
    )
    ethanol_average_price = graphene.Float(
        description='Ethanol average price for the region in the last 15 days'
    )
    ethanol_lowest_price = graphene.Float(
        description='Ethanol lowest price for the region in the last 15 days'
    )
    ethanol_highest_price = graphene.Float(
        description='Gasoline highest price for the region in the last 15 days'
    )
    date_reference = graphene.Date(
        description='Date the data was gathered'
    )

    def resolve_gasoline_average_price(self, info, **kwargs):
        return self.gas_price

    def resolve_gasoline_lowest_price(self, info, **kwargs):
        return self.gas_lower_price

    def resolve_gasoline_highest_price(self, info, **kwargs):
        return self.gas_higher_price

    def resolve_ethanol_average_price(self, info, **kwargs):
        return self.ethanol_price

    def resolve_ethanol_lowest_price(self, info, **kwargs):
        return self.ethanol_lower_price

    def resolve_ethanol_highest_price(self, info, **kwargs):
        return self.ethanol_higher_price

    def resolve_date_reference(self, info, **kwargs):
        return self.datetime_reference


class Query(graphene.ObjectType):
    gas_prices = graphene.List(GasPriceType)

    def resolve_gas_prices(self, info, **kwargs):
        return GasPrice.objects.filter(**kwargs)
