import graphene
from houses.models import HouseOffer


class HouseOfferType(graphene.ObjectType):
    price = graphene.Float()
    url = graphene.String()
    description = graphene.String()
    category = graphene.String()
    type = graphene.String()
    condominium = graphene.Float()
    property_tax = graphene.Float(description='PT-BR: Valor do IPTU do Imóvel')
    useful_area = graphene.String()
    bedrooms = graphene.Int()
    bathrooms = graphene.Int()
    parking_spaces = graphene.Int()
    postal_code = graphene.String(description='PT-BR: CEP')
    county = graphene.String()
    district = graphene.String()
    address = graphene.String()
    date_reference = graphene.Date()


class Query(graphene.ObjectType):
    house_offers = graphene.List(
        HouseOfferType,
        description='EN: Query house offers | PT-BR: Lista ofertas de Imóveis'
    )

    def resolve_house_offers(self, info, **kwargs):
        return HouseOffer.objects.filter(**kwargs)
