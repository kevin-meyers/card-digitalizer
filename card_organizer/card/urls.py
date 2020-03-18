from django.urls import path

from card.views import CardList

urlpatterns = [
    path('api/card/', CardList.as_view()),
]
