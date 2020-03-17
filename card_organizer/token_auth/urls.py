from django.urls import path
from token_auth.views import current_user, UserList


app_name='auth'
urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]
