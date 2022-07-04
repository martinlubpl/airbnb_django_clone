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


class SignUpForm(forms.ModelForm):

    # Meta is required for modelforms
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            # "password1",
            # "password2",
        ]

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
    # clean_email unnessesary-ModelForm cleans it. but nneds clean_pass to check passes are equal

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, *args, **kwargs):

        # dont commit to db
        user = super().save(commit=False)
        # email is username
        user.username = self.cleaned_data.get("email")
        user.set_password(self.cleaned_data.get("password1"))
        user.save()  # commit to db
