import graphene
from django.conf import settings
from bmw.models import BMWOffer


class BMWOfferType(graphene.ObjectType):
        price = graphene.Float()
        url = graphene.String()
        car_model = graphene.String()
        car_year = graphene.Int()
        km = graphene.Int()
        power = graphene.String()
        color = graphene.String()
        seller_name = graphene.String()


class Query(graphene.ObjectType):
    version = graphene.String()

    def resolve_version(self, info, **kwargs):
        return settings.VERSION

    # BMWOffer
    bmw_offers = graphene.List(
        BMWOfferType,
        car_year=graphene.Int(description='Filter by car year'),
        car_year__lte=graphene.Int(
            description='Filter cars by year less equal a value'
        ),
        car_year__gte=graphene.Int(
            description='Filter cars by year greater equal a value'
        ),
        price=graphene.Float(description='Filter by car price'),
        price__lte=graphene.Float(
            description='Filter cars by price less equal a value'
        ),
        price__gte=graphene.Float(
            description='Filter cars by price greater equal a value'
        ),
        km=graphene.Int(description='Filter by car engine usage'),
        km__lte=graphene.Int(
            description='Filter cars by engine usage less equal a value'
        ),
        km__gte=graphene.Int(
            description='Filter cars by engine usage greater equal a value'
        ),
        color=graphene.String(description='Filter by car specific color'),
    )

    def resolve_bmw_offers(self, info, **kwargs):
        bm =  BMWOffer.objects.filter(**kwargs)
        return bm
