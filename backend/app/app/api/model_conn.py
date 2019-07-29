import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import (Repositories as ReposModel, RepositoryFields as RepoFieldsModel,
                        RepositoryFieldTypes as RepoFieldTypesModel,
                        NumericalFieldProperties as NumericalFieldPropsModel,
                        PlainTextFieldProperties as PlainTextFieldPropsModel, NumericalData as NumericalDataModel,
                        PlainTextData as PlainTextDataModel, Items as ItemsModel)

schema = ''


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    repos = 


class Repos(SQLAlchemyObjectType):
    class Meta:
        model = ReposModel
        interfaces = (relay.Node, )


class ReposConnection(relay.Connection):
    class Meta:
        node = Repos


class ReposFields(SQLAlchemyObjectType):
    class Meta:
        model = RepoFieldsModel
        interfaces = (relay.Node, )


class ReposFieldsConnection(relay.Connection):
    class Meta:
        node = ReposFields


class ReposFieldTypes(SQLAlchemyObjectType):
    class Meta:
        model = RepoFieldTypesModel
        interfaces = (relay.Node, )


class ReposFieldTypesConnection(relay.Connection):
    class Meta:
        node = ReposFieldTypes


class NumericalFieldProperties(SQLAlchemyObjectType):
    class Meta:
        model = NumericalFieldPropsModel
        interfaces = (relay.Node, )


class NumericalFieldPropertiesConnection(relay.Connection):
    class Meta:
        node = NumericalFieldProperties


class PlainTextFieldProperties(SQLAlchemyObjectType):
    class Meta:
        model = PlainTextFieldPropsModel
        interfaces = (relay.Node, )


class PlainTextFieldPropertiesConnection(relay.Connection):
    class Meta:
        node = PlainTextFieldProperties


class PlainTextData(SQLAlchemyObjectType):
    class Meta:
        model = PlainTextDataModel
        interfaces = (relay.Node, )


class PlainTextDataConnection(relay.Connection):
    class Meta:
        node = PlainTextData


class NumericalData(SQLAlchemyObjectType):
    class Meta:
        model = NumericalDataModel
        interfaces = (relay.Node, )


class NumericalDataConnection(relay.Connection):
    class Meta:
        node = NumericalData


class Items(SQLAlchemyObjectType):
    class Meta:
        model = ItemsModel
        interfaces = (relay.Node, )


class ItemsConnection(relay.Connection):
    class Meta:
        node = Items
