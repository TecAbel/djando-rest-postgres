from typing import Generic, TypeVar

from rest_framework import serializers

from .models import Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'name', 'description')
        model = Roles
        fields = "__all__"


T = TypeVar("T")


class BaseResponse(Generic[T]):
    message: str
    data: serializers.ReturnDict

    def __init__(self, message: str, data: serializers.ModelSerializer):
        self.message = message
        self.data = data.data

    def toJson(self):
        return {"message": self.message, "data": self.data}


class CustomSerializer(serializers.Serializer):
    message = serializers.CharField()
    data = serializers.ListSerializer(child=RolesSerializer())
