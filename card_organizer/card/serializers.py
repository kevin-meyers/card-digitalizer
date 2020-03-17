from rest_framework import serializers

from card.models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'name', 'type_1', 'type_2', 'price', 'year_released')
