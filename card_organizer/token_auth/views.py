from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import TokenError

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """
    token = request.COOKIES.get('jwt_token')

    return Response(status=status.HTTP_200_OK)


class SignUp(APIView):
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

        # For the love of god dont this for long
        #TODO: Help please lol, I am doing this because of upcoming deadline
        # And I want to show off features without there being all this pain
        response.set_cookie('username', username)


        return response


class Login(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        tokens = serializer.validated_data

        response = Response(request.data['username'], status=status.HTTP_200_OK)
        response.set_cookie('jwt_token', tokens['access'])
        response.set_cookie('refresh_token', tokens['refresh'])

        #TODO GET RID OF
        response.set_cookie('username', request.data['username'])

        return response

class RefreshToken(TokenRefreshView):
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get('refresh_token')
        serializer = self.get_serializer(data={'refresh': token})
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        response = Response(status=status.HTTP_200_OK)
        response.set_cookie('jwt_token', serializer.validated_data['access'])

        return response
