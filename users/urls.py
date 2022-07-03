# from django import urls
from django.urls import path
from .views import LoginView

app_name = "users"  # namespace for config urls


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
]
