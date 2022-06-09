# from django.db import models
from core.models import TimeStampModel

# Create your models here.


class Room(TimeStampModel):
    """Room Model"""

    # name = models.CharField(max_length=128)
    # description = models.TextField()

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    pass
