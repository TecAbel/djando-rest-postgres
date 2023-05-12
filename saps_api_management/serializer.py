from typing import Generic, TypeVar

from rest_framework import serializers
from rest_framework.response import Serializer

T = TypeVar("T")


class BaseResponse(Generic[T]):
    message: str
    content: T

    def __init__(self, message: str, content: Serializer[T]):
        self.message = message
        self.content = content

    def toJson(self):
        return {"message": self.message, "content": self.content}


class BaseActionResponse(serializers.Serializer):
    message = serializers.CharField()
    content = serializers.BooleanField()
