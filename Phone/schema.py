import graphene

from graphene import relay, ObjectType

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Text, Color

class TextNode(DjangoObjectType):
    class Meta:
        model = Text
        filter_fields = {
            'txt'
        }