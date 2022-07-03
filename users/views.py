from django.shortcuts import render

from django.views import View
from .forms import LoginForm

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = LoginForm(
            initial={"email": "martinpl@gmai.com"}
        )  # init for testing purposes only
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        return render(request, "users/login.html", {"form": form})
