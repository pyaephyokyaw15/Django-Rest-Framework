from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from .test import CustomAuthToken

urlpatterns = [
    path('auth/', CustomAuthToken.as_view()),
    path('', views.api_home),
]