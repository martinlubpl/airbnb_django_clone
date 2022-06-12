from django.contrib import admin
from .models import Conversation, Message

# Register your models here.


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Conversations Admin"""

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Messages Admin"""

    list_display = ("__str__", "created")
