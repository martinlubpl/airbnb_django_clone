from django.contrib import admin
from .models import Room, RoomType


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass
