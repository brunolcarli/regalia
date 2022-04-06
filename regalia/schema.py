import graphene

import bmw.schema
import gas.schema

class Query(bmw.schema.Query, gas.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
