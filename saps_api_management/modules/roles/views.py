from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView

from ...models import Roles
from ...serializer import BaseActionResponse, BaseResponse
from .serializers import RoleListResponse, RoleRequest, RolesSerializer


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
