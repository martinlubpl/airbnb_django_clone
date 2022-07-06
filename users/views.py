# import email
import os
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
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


def github_callback(request):
    pass
