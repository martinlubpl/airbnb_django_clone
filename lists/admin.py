from django.contrib import admin
from .models import List

# Register your models here.


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    """List Admin Model"""

    pass
