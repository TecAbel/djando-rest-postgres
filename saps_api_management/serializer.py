from typing import Generic, TypeVar

from rest_framework import serializers

T = TypeVar("T")


class BaseResponse(Generic[T]):
    message: str
    content: serializers.ReturnDict

    def __init__(self, message: str, content: serializers.ModelSerializer):
        self.message = message
        self.content = content.data

    def toJson(self):
        return {"message": self.message, "content": self.content}


class BaseActionResponse(serializers.Serializer):
    message = serializers.CharField()
    content = serializers.BooleanField()
