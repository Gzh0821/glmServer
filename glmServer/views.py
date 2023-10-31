from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@swagger_auto_schema(
    method='GET',

    responses={
        200: openapi.Response("No, Never, Because..."),
        418: openapi.Response("I'm a teapot."),
    }
)
@api_view(['GET'])
def teapot(request):
    return Response({"detail": "I'm a teapot."},
                    status=status.HTTP_418_IM_A_TEAPOT)
