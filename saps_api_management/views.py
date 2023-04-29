from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Roles
from .serializer import BaseResponse, RolesSerializer

# Create your views here.


class RolesList(APIView):
    def get(self, __):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)
        response = BaseResponse[RolesSerializer](
            message="Roles obtenidos correctamente",
            data=serializer,
        )
        return Response(response.toJson())
