from django.db import models
from core.models import TimeStampModel

# Create your models here.


class Review(TimeStampModel):
    """Review Model"""

    # text review
    review = models.TextField()
    # ratings
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    # user
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # room
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room.name} - {self.room.host.email}"
