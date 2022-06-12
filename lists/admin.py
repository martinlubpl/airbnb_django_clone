from django.contrib import admin
from .models import List

# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Model"""

    list_display = (
        "name",
        "user",
        "count_rooms",
    )
    search_fields = (
        "name",
        "user__username",
        "room__name",
    )

    filter_horizontal = ("room",)
