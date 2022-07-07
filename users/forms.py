from django import forms
from django.contrib.auth.forms import UserCreationForm
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


# signup using built-in forms

# https://docs.djangoproject.com/en/4.0/topics/auth/default/#module-django.contrib.auth.forms
class SignUpForm(UserCreationForm):
    # disguise the email field as username
    username = forms.EmailField(label="Email")

    """ class Meta:
        model = User
        fields = ("email",) """

    # use: from django.contrib.auth import password_validation
    # if not using built-in forms to validate pass

    """ try:
        password_validation.validate_password(password)
    except forms.ValidationError as error:
        self.add_error("password", error) """
