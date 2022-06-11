from django.contrib import admin
from .models import Review

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Review Admin"""

    # list_display = (
    #     "room",
    #     "user",
    #     "accuracy",
    #     "communication",
    #     "cleanliness",
    #     "location",
    #     "check_in",
    #     "value",
    # )

    pass
