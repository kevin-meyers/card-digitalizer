from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
