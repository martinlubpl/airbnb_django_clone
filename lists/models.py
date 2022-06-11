from django.db import models

from core.models import TimeStampModel

# Create your models here.


class List(TimeStampModel):
    """List Model"""

    name = models.CharField(max_length=128)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    room = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name
