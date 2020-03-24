from rest_framework import serializers

from card.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ('id', 'user', 'name', 'stage', 'series', 'rarity', 'type_1',
                  'type_2', 'image_url')

