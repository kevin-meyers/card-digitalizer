from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=100)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, null=True, blank=True)

    price = models.FloatField()
    year_released = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

