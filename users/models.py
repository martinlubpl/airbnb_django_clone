# from locale import currency
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your models here.


class User(AbstractUser):
    """Custom user model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_POLISH = "pl"
    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "English"), (LANGUAGE_POLISH, "Polish"))

    CURRENCY_USD = "usd"
    CURRENCY_PLN = "pln"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_PLN, "PLN"))

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, blank=True, default="other"
    )
    bio = models.TextField(blank=True)
    # bio = models.TextField(null=True) # can be empty
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="en", max_length=2, blank=True
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES, default="usd", max_length=3, blank=True
    )

    superhost = models.BooleanField(default=False)

    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=32, default="", blank=True)

    def email_verification(self):
        """verify email"""
        if not self.email_confirmed:
            self.email_secret = uuid.uuid4().hex
            html_message = render_to_string(
                "emails/verify.html", {"secret": self.email_secret}
            )
            send_mail(
                "Please verify your MMbnb email",
                "To verify your email, visit http://127.0.0.1:8000/users/verify/"
                + self.email_secret,
                settings.EMAIL_HOST_USER,
                [self.email],
                fail_silently=False,
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD,
                html_message=html_message,
            )
            self.save()  # remember to save omg !!!
        return

    def __str__(self):
        return "user: " + self.username
