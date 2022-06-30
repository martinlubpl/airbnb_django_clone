from django.db import models
from django.urls import reverse
from django_countries.fields import CountryField
from core.models import TimeStampModel

# Create your models here.


class AbstractItem(TimeStampModel):
    """Abstract Item"""

    name = models.CharField(max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """Room Type Model"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]


class Amenity(AbstractItem):
    """Amenity Model"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """House Rule Model"""

    class Meta:
        verbose_name = "House Rule"


# ! inherit from abstract TimeStampModel


class Room(TimeStampModel):
    """Room Model"""

    # name = models.CharField(max_length=128)
    # description = models.TextField()

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128)
    description = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=128)
    price = models.IntegerField()
    address = models.CharField(max_length=128)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey(
        RoomType, related_name="rooms", blank=True, on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return "room: " + self.name

    # overriding save
    def save(self, *args, **kwargs):
        self.city = self.city.title()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:room_detail", kwargs={"pk": self.pk})

    def get_room_average(self):
        all_reviews = self.reviews.all()
        all_ratings = []

        for review in all_reviews:
            all_ratings.append(review.get_avg())
        # div by 0
        if len(all_ratings) == 0:
            return 3.0
        return round(sum(all_ratings) / len(all_ratings), 2)

    get_room_average.short_description = "Room Rating"


class Photo(TimeStampModel):
    """Photo Model"""

    caption = models.CharField(max_length=128)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(Room, related_name="photos", on_delete=models.CASCADE)
    # or use "Room" instead of Room.

    def __str__(self):
        return self.caption
