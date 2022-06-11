from django.contrib import admin
from .models import Reservation

# Register your models here.


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """Reservation Admin"""

    # list_display = (
    #     "room",
    #     "status",
    #     "guest",
    #     "check_in",
    #     "check_out",
    #     "created",
    #     "modified",
    # )
    pass
