from typing import Generic, TypeVar

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'name', 'description')
        model = Roles
        fields = "__all__"


T = TypeVar("T")


class BaseResponse(Generic[T]):
    message: str
    data: T

    def __init__(self, message: str, data: T):
        self.message = message
        self.data = data

    def toJson(self):
        return {"message": self.message, "data": self.data}


# BaseResponse = TypedDict({
#     "message": str,
#     "data"
#     })
