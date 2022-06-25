from django.contrib import admin
from django.utils.html import mark_safe
from .models import Facility, Room, RoomType, Amenity, HouseRule, Photo


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin"""

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Time", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Space", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Host", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        # "description",
        "get_room_average",  # def in .models.Room
        "country",
        "city",
        "price",
        "address",
        "beds",
        "bedrooms",
        "baths",
        "guests",
        "instant_book",
        "host",
        "room_type",
        "count_amenities",  # fun call to count_amenities
        "count_photos",  # also a fun
    )

    ordering = (
        "name",
        "price",
    )

    list_filter = (
        "instant_book",
        "host__superhost",  # use __ instead of .
        "host__gender",
        "host",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    filter_horizontal = ("amenities", "facilities", "house_rules")

    search_fields = ("city", "name", "description", "host__username")
    # "^city"
    # /ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    # "host__username" __ instead of . for foreign key

    def count_amenities(self, obj):  # obj is current row of RoomAdmin
        return obj.amenities.count()
        # return "aaa"

    def count_photos(self, obj):
        return obj.photos.count()

    count_amenities.short_description = "Am-ties Count"


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin"""

    list_display = (
        "name",
        "count_rooms",
    )

    def count_rooms(self, obj):
        return obj.rooms.count()

    pass


# @admin.register(Facility)
# class FacilityAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Amenity)
# class AmenityAdmin(admin.ModelAdmin):
#     pass


# @admin.register(HouseRule)
# class HouseRuleAdmin(admin.ModelAdmin):
#     pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo admin"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumb"
