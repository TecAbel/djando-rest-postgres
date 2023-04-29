from rest_framework.response import Response
from rest_framework.serializers import ReturnDict
from rest_framework.views import APIView

from .models import Roles
from .serializer import BaseResponse, RolesSerializer

# Create your views here.


# class RolesViewSet(viewsets.ModelViewSet):
#     serializer_class = RolesSerializer
#     queryset = Roles.objects.all()

# @csrf_exempt
# @api_view(['GET', 'POST'])
# def roles_list(request):
#     if request.method == 'GET':
#         roles = Roles.objects.all()
#         serializer = RolesSerializer(roles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = RolesSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.error_messages, status=400)


class RolesList(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)
        response = BaseResponse[ReturnDict](message="ok", data=serializer.data)
        # return Response({"message": "ok", "data": serializer.data})
        return Response(response.toJson())
