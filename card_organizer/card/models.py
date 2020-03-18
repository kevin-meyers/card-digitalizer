from django.db import models
from django.conf import settings



class Card(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, null=True, blank=True)

    price = models.FloatField(max_length=20)
    year_released = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Pokemon(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=20)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, null=True)

    series = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)

    year_released = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


