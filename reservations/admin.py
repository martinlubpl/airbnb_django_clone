from django.contrib import admin
from .models import Reservation

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation Admin"""

    list_display = (
        "room",
        "status",
        "guest",
        "in_progress",  # def in .models.Reservation
        "is_finished",  # def in .models.Reservation
        "check_in",
        "check_out",
        "created",
        "updated",
    )

    list_filter = (
        "status",
        "created",
        "updated",
    )
