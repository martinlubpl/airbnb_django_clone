from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.

# admin.site.register(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "language",
        "currency",
        "superhost",
    )

    list_filter = UserAdmin.list_filter + (
        "superhost",
        "language",
        "currency",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    ordering = ("-date_joined",)

    # OLD WAY
    # list_display = ("username", "email", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "superhost",
    #     "language",
    #     "currency",
    # )
