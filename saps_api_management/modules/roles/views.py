from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView

from ...models import Roles
from ...serializer import BaseResponse
from .serializers import RoleListResponse, RolesSerializer


class RolesList(APIView):
    @extend_schema(responses=RoleListResponse)
    def get(self, _):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)
        rdata = BaseResponse[RolesSerializer](message="ok", content=serializer)
        response = RoleListResponse(rdata)
        return Response(response.data)
