from django import forms
from .models import User


class LoginForm(forms.Form):

    # set username to email
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # cannot use PasswordInput directly

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(email=email)
            # check_password => True if the given raw string is the correct
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is incorrect")
                )
        except User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))
