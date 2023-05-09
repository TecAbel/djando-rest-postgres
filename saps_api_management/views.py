# Create your views here.

from django.http.response import HttpResponseRedirect
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView


class BaseView(APIView):
    @extend_schema(exclude=True)
    def get(self, _):
        return HttpResponseRedirect(redirect_to="/docs")
