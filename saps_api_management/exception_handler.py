from rest_framework.serializers import ErrorDetail
from rest_framework.views import exception_handler
from rest_framework.response import Response
from .serializer import BaseActionResponse


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if isinstance(response, Response):
        if response.data is None:
            return response
        response.data["status_code"] = response.status_code
        print(response.data["detail"])
        serializer = BaseActionResponse(
            {"message": ErrorDetail(response.data["detail"]), "content": None}
        )
        return Response(data=serializer.data, status=response.status_code)

    return response
