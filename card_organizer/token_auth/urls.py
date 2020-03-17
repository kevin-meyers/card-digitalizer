from django.urls import path
from token_auth.views import current_user, CreateUser


app_name='auth'
urlpatterns = [
    path('current_user/', current_user),
    path('create_user/', CreateUser.as_view())
]
