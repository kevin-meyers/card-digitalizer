from django.shortcuts import render

from card.models import Card
from card.serializers import CardSerializer
from rest_framework import generics

class CardListCreate(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

