from django.shortcuts import render
from django.contrib.auth.models import User

from card.models import Pokemon
from card.serializers import PokemonSerializer
from rest_framework import generics, authentication, permissions

from rest_framework_simplejwt.backends import TokenBackend

tb = TokenBackend('HS256')


class myAuth(authentication.TokenAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt_token')
        data = tb.decode(token, verify=None)
        print(data)
        auth = ['Token', data['jti']]

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)


class PokemonList(generics.ListAPIView):
    serializer_class = PokemonSerializer
    authentication_classes = []  # [myAuth]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        username = self.request.COOKIES.get('username')
        user = User.objects.get(username=username)

        return Pokemon.objects.filter(user=user)

class PokemonCreate(generics.CreateAPIView):
    serializer_class = PokemonSerializer
    authentication_classes = [] # Remove parent auth
    permission_classes = [permissions.AllowAny] # because I dont have enough time

    def create(self, request, *args, **kwargs):
        username = self.request.COOKIES.get('username')
        user = User.objects.get(username=username)

        request.data['user'] = user.id

        return super().create(request, *args, **kwargs)

