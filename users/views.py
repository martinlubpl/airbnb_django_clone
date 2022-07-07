import os
import requests
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy

# from django.shortcuts import redirect
# from django.views import View
from .forms import LoginForm, SignUpForm
from users.models import User

# Create your views here.


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:home")
    initial = {
        "email": "martinpl@gmail.com",  # only for testing
    }

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user:  # if user is not None
            login(self.request, user)
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect("core:home")


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    # just for testing
    initial = {
        "first_name": "Marcin",
        "last_name": "Majewski",
        "email": "smdesign.eu@gmail.com",
    }

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=email, password=password)
        if user:
            login(self.request, user)
        # send email with mailgun
        user.email_verification()
        return super().form_valid(form)


def complete_verification(request, uuid):
    # .get(email_secret=uuid)
    user = User.objects.filter(email_secret=uuid).first()
    if user:
        user.email_confirmed = True
        user.email_secret = ""
        user.save()
        login(request, user)
        # todo: success message
    else:
        pass
        # todo: error message

    return redirect("core:home")


def login_github(request):

    # github settings => dev settings => oauth apps => new oauth app
    client_id = os.environ.get("GITHUB_CLIENT_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"

    # https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&"
        + f"redirect_uri={redirect_uri}&scope=read:user"
    )


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        code = request.GET.get("code", None)
        if code:
            # requests lib
            request_token = requests.post(
                "https://github.com/login/oauth/access_token",
                data={
                    "client_id": os.environ.get("GITHUB_CLIENT_ID"),
                    "client_secret": os.environ.get("GITHUB_SECRET"),
                    "code": code,
                },
                headers={"Accept": "application/json"},  # request json format
            )
            # all described at
            # https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps

            result = request_token.json()
            error = result.get("error", None)
            if error:
                raise GithubException(error)
            else:
                access_token = result.get("access_token", None)
                if access_token:
                    # get user from gh API
                    api_request = requests.get(
                        "https://api.github.com/user",
                        headers={
                            "Authorization": f"token {access_token}",
                            "Accept": "application/json",
                        },
                    )
                    api_result = api_request.json()
                    username = api_result.get("login", None)
                    email = api_result.get("email", None)
                    # print(api_result)
                    if username and email:  # ! some github users don't have email

                        # print(api_result)
                        name = api_result.get("name", None)

                        # print(f"!!!{email}")
                        bio = api_result.get("bio", None)

                        try:
                            user_try = User.objects.get(email=email)
                            if user_try.login_method == User.LOGIN_GITHUB:
                                # returning github user
                                login(request, user_try)
                                return redirect("core:home")
                            else:
                                raise GithubException("Please logout first")
                        except User.DoesNotExist:
                            new_user = User.objects.create(
                                username=email,
                                first_name=name,
                                email=email,
                                bio=bio,
                                login_method=User.LOGIN_GITHUB,
                            )
                            # https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#django.contrib.auth.models.User.set_unusable_password
                            new_user.set_unusable_password()
                            new_user.save()
                            login(request, new_user)
                        # outside  try except
                        return redirect("core:home")

                    else:  # no username
                        raise GithubException("No username or no email")

        else:  # if code is None
            raise GithubException

    except GithubException as e:
        print(e)
        return redirect("users:login")
