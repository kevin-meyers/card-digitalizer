from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)

    return Response(serializer.data)


class CreateUser(APIView):
    """
    Create a new user.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        tokens = serializer.data['token']
        username = serializer.data['username']

        response = Response(username, status=status.HTTP_201_CREATED)
        response.set_cookie('jwt_token', tokens['access'])
        response.set_cookie('refresh_token', tokens['refresh'])


        return response

