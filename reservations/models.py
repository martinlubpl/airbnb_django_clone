from django.db import models
from django.utils import timezone
from core.models import TimeStampModel

# Create your models here.


class Reservation(TimeStampModel):
    """Reservation model"""

    status = models.CharField(
        max_length=20,
        choices=(
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ),
        default="pending",
    )

    # todo STATUS_PENDING  = 'pending' ...etc
    # then STATUS_CHOICES = (

    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.room} - {self.check_in} to {self.check_out}"

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    in_progress.boolean = True
    in_progress.short_description = "now?"

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True
    is_finished.short_description = "ended?"
