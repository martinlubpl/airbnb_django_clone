# from django import urls
from django.urls import path
from .views import (
    LoginView,
    complete_verification,
    github_callback,
    logout_view,
    SignUpView,
    login_github,
)

app_name = "users"  # namespace for config urls


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("verify/<str:uuid>", complete_verification, name="verify"),
    path("loging/github/", login_github, name="login_github"),
    path("loging/github/callback", github_callback, name="github_callback"),
]
