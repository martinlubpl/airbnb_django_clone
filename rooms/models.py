from django.db import models

from django_countries.fields import CountryField
from core.models import TimeStampModel

# Create your models here.

# ! inherit from abstract TimeStampModel


class Room(TimeStampModel):
    """Room Model"""

    # name = models.CharField(max_length=128)
    # description = models.TextField()

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128)
    description = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=128)
    price = models.IntegerField()
    address = models.CharField(max_length=128)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return "room: " + self.name
