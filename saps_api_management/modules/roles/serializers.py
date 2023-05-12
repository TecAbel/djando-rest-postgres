from typing import Iterable, List
from ...models import Roles
from rest_framework import serializers


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'name', 'description')
        model = Roles
        fields = "__all__"


class RoleListResponse:
    message: str
    content: Iterable[Roles]

    def __init__(self, message: str, content: Iterable[Roles]) -> None:
        self.message = message
        self.content = content


class RoleListResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    content = serializers.ListField(child=RolesSerializer())


class RoleRequest(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False)


class RoleSingleResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    content = RolesSerializer()


class RoleSingleResponse:
    message: str
    content: Roles

    def __init__(self, message: str, content: Roles) -> None:
        self.message = message
        self.content = content


class RetrieveParams(serializers.Serializer):
    name = serializers.CharField(required=False)
