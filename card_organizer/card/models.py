from django.db import models
from django.conf import settings


class Pokemon(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    card_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=20)
    type_1 = models.CharField(max_length=20)
    type_2 = models.CharField(max_length=20, null=True, blank=True)

    series = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)

    image_url = models.URLField()

    year_released = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


