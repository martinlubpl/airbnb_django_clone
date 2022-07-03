from django import forms
from .models import User


class LoginForm(forms.Form):

    # set username to email
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # cannot use PasswordInput directly

    # clean_<fieldname>
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            # ! not email=email since username is email
            user = User.objects.get(username=email)
            return email
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    # def clean(self): can also be used
