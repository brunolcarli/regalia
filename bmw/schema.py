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
    bmw_offers = graphene.List(BMWOfferType)

    def resolve_bmw_offers(self, info, **kwargs):
        bm =  BMWOffer.objects.filter(**kwargs)
        return bm
