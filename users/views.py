import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
from django.urls import reverse_lazy

# from django.shortcuts import redirect
# from django.views import View
from .forms import LoginForm

# Create your views here.


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("core:home")
    initial = {
        email: "martinpl@gmail.com",  # only for testing
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
