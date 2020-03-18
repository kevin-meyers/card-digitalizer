from django.shortcuts import render
from django.contrib.auth.models import User

from card.models import Card, Pokemon
from card.serializers import CardSerializer
from rest_framework import generics

from rest_framework_simplejwt.backends import TokenBackend

tb = TokenBackend('HS256')

class CardList(generics.ListAPIView):
    serializer_class = CardSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('jwt_token')
        data = tb.decode(token, verify=None)

        user_id = data['user_id']
        user = User.objects.get(id=user_id)

        return Card.objects.filter(user=user)

class PokemonCreate(generics.CreateAPIView):
    pass
