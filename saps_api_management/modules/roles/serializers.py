from ...models import Roles
from rest_framework import serializers


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'name', 'description')
        model = Roles
        fields = "__all__"


class RoleListResponse(serializers.Serializer):
    message = serializers.CharField()
    content = serializers.ListField(child=RolesSerializer())
