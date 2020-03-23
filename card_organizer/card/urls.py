from django.urls import path

from card.views import CardList, PokemonCreate

urlpatterns = [
    path('api/card/', CardList.as_view()),
    path('api/card/create', PokemonCreate.as_view()),
]
