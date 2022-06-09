# from locale import currency
from django.contrib.auth.models import AbstractUser
from django.db import models

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
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    # bio = models.TextField(null=True) # can be empty
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="english", max_length=2, blank=True
    )

    currency = models.CharField(
        choices=CURRENCY_CHOICES, default="usd", max_length=3, blank=True
    )

    superhost = models.BooleanField(default=False)

    def __str__(self):
        return "user: " + self.username
