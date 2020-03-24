from django.urls import path

from card.views import PokemonList, PokemonCreate

urlpatterns = [
    path('api/card/list', PokemonList.as_view()),
    path('api/card/create', PokemonCreate.as_view()),
]
