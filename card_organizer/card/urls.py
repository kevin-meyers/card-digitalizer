from django.urls import path

from card.views import CardListCreate

urlpatterns = [
    path('api/card/', CardListCreate.as_view()),
]
