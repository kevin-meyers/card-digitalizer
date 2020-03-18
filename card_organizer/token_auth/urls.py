from django.urls import path
from token_auth.views import (
    current_user,
    CreateUser,
    Login,
    RefreshToken,
)


urlpatterns = [
    path('current_user/', current_user),
    path('create_user/', CreateUser.as_view()),
    path('token/', Login.as_view()),
    path('token/refresh/', RefreshToken.as_view()),
]
