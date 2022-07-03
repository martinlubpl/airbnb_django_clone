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
            User.objects.get(username=email)
            return email
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=email)
            # check_password => True if the given raw string is the correct
            if user.check_password(password):
                return password
            else:
                raise forms.ValidationError("Password is incorrect")
        except User.DoesNotExist:
            pass

    # def clean(self): can also be used
