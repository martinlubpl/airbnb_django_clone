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
        chat_users = []
        for usr in self.participants.all():
            chat_users.append(usr.username)
        return f"Conversation between {', '.join(chat_users)}"

    def count_messages(self):
        return self.messages.count()  # related_name

    count_messages.short_description = "# of Messages"

    def count_participants(self):
        return self.participants.count()  # related_name

    count_participants.short_description = "# of Participants"


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
