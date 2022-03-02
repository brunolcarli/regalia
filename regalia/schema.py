import graphene

import bmw.schema


class Query(bmw.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
