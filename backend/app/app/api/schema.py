import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from app.api.model_conn import (ReposConnection, RepoFieldsConnection, ReposFieldTypesConnection,
                                NumericalFieldPropsConnection, PlainTextFieldPropsConnection, PlainTextDataConnection,
                                NumericalDataConnection, ItemsConnection)


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    repos = SQLAlchemyConnectionField(ReposConnection, sort=None)
    repo_fields = SQLAlchemyConnectionField(RepoFieldsConnection, sort=None)
    repo_field_types = SQLAlchemyConnectionField(ReposFieldTypesConnection, sort=None)
    numerical_field_props = SQLAlchemyConnectionField(NumericalFieldPropsConnection, sort=None)
    plain_text_field_props = SQLAlchemyConnectionField(PlainTextFieldPropsConnection, sort=None)
    plain_text_data = SQLAlchemyConnectionField(PlainTextDataConnection, sort=None)
    numerical_data = SQLAlchemyConnectionField(NumericalDataConnection, sort=None)
    items = SQLAlchemyConnectionField(ItemsConnection, sort=None)


schema = graphene.Schema(query=Query)