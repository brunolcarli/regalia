import graphene

import bmw.schema
import gas.schema
import houses.schema


class Query(
    bmw.schema.Query,
    gas.schema.Query,
    houses.schema.Query,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
