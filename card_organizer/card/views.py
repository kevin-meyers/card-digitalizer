from django.shortcuts import render
from django.contrib.auth.models import User

from card.models import Pokemon
from card.serializers import PokemonSerializer
from rest_framework import generics, authentication, permissions

from rest_framework_simplejwt.backends import TokenBackend

tb = TokenBackend('HS256')

class PokemonList(generics.ListAPIView):
    serializer_class = PokemonSerializer
    authentication_classes = []  # [myAuth]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        username = self.request.COOKIES.get('username')
        print(username)
        print(self.request.COOKIES)
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

