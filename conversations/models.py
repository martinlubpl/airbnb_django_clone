from django.db import models

from core.models import TimeStampModel

# Create your models here.


class Conversation(TimeStampModel):
    """
    Conversation Model
    """

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        return f"{self.created} - {self.participants.all()}"


class Message(TimeStampModel):
    """
    Message Model
    """

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.message}"
