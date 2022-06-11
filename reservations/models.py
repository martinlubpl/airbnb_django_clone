from django.db import models

from core.models import TimeStampModel

# Create your models here.


class Reservation(TimeStampModel):
    """Reservation model"""

    STATUS = models.CharField(
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
