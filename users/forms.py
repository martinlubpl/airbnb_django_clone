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


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        min_length=8,
        max_length=20,
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
        min_length=8,
        max_length=20,
    )

    # clean_<field_name>
    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("User with this email already exists")
        except User.DoesNotExist:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2
