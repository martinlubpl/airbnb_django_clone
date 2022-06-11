from django.contrib import admin
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
    # "host__username" __ instead of . because it's a foreign key


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin"""

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

    pass
