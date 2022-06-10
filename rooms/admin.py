from django.contrib import admin
from .models import Facility, Room, RoomType, Amenity, HouseRule


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
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
