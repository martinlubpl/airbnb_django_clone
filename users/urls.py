# from django import urls
from django.urls import path
from .views import LoginView, complete_verification, logout_view, SignUpView

app_name = "users"  # namespace for config urls


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify/<str:uuid>", complete_verification, name="verify"),
]
