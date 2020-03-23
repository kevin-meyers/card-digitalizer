from rest_framework import serializers

from card.models import Card, Pokemon


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'type_1', 'type_2', 'price', 'year_released')


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'user','name', 'stage', 'series', 'rarity', 'type_1', 'type_2')

