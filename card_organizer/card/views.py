from django.shortcuts import render
from django.contrib.auth.models import User

from card.models import Card, Pokemon
from card.serializers import CardSerializer, PokemonSerializer
from rest_framework import generics

from rest_framework_simplejwt.backends import TokenBackend

tb = TokenBackend('HS256')

class CardList(generics.ListAPIView):
    serializer_class = PokemonSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('jwt_token')
        data = tb.decode(token, verify=None)

        user_id = data['user_id']

        return Pokemon.objects.filter(user=user_id)

class PokemonCreate(generics.CreateAPIView):
    serializer_class = PokemonSerializer

    def create(self, request, *args, **kwargs):
        token = self.request.COOKIES.get('jwt_token')
        data = tb.decode(token, verify=None)

        user_id = data['user_id']

        request.data['user'] = user_id

        return super().create(request, *args, **kwargs)

