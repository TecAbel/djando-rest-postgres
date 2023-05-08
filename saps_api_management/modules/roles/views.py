from django.core.exceptions import BadRequest
from django.http import request
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import NotFound, ValidationError, status
from rest_framework.fields import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.views import APIView

from ...models import Roles
from ...serializer import BaseActionResponse, BaseResponse
from .serializers import (
    RoleListResponse,
    RoleRequest,
    RoleSingleResponse,
    RolesSerializer,
)


class RolesList(APIView):
    @extend_schema(responses=RoleListResponse)
    def get(self, _):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)
        rdata = BaseResponse[RolesSerializer](message="ok", content=serializer)
        response = RoleListResponse(rdata)
        return Response(response.data)

    @extend_schema(request=RoleRequest, responses=BaseActionResponse)
    def post(self, request):
        serializer = RolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = BaseActionResponse(
                {
                    "message": "Role added successfully",
                    "content": True,
                }
            )
            return Response(response.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetail(APIView):
    def get_object(self, pk: int):
        try:
            role = Roles.objects.get(id=pk)
            return role
        except ObjectDoesNotExist:
            raise NotFound(detail="Role not found")

    @extend_schema(
        responses={
            200: RoleSingleResponse,
            400: BaseActionResponse,
            404: BaseActionResponse,
        }
    )
    def get(self, request, pk: int, format=None):
        role = self.get_object(pk)
        serializer = RolesSerializer(role)
        rdata = BaseResponse[RolesSerializer](
            message="Gor role successfully", content=serializer
        )
        response = RoleSingleResponse(rdata)
        return Response(response.data)

    @extend_schema(request=RoleRequest, responses={200: BaseActionResponse})
    def put(self, request, pk: int, format=None):
        role = self.get_object(pk)
        serializer = RolesSerializer(role, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = BaseActionResponse({"message": "Role updated", "content": True})
            return Response(res.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
