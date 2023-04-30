from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import status
from rest_framework.fields import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.views import APIView, Http404
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
            print("role" + role)
            return role
        except ObjectDoesNotExist:
            print("on catch")
            res = BaseActionResponse({"message": "Role not found", "content": False})
            print(res.data)
            return Response(data=res.data, status=HTTP_404_NOT_FOUND)

    @extend_schema(
        responses={
            200: RoleSingleResponse,
            400: BaseActionResponse,
            404: BaseActionResponse,
        }
    )
    def get(self, request, pk: int, format=None):
        role = self.get_object(pk)
        if isinstance(role, Response):
            return role
        serializer = RolesSerializer(role)
        rdata = BaseResponse[RolesSerializer](
            message="Gor role successfully", content=serializer
        )
        response = RoleSingleResponse(rdata)
        return Response(response.data)
