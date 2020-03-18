from django.urls import path
from token_auth.views import (
    current_user,
    SignUp,
    Login,
    RefreshToken,
)


urlpatterns = [
    path('current_user/', current_user),
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view()),
    path('token/refresh/', RefreshToken.as_view()),
]
