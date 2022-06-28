from rooms import views as room_views
from django.urls import path

app_name = "core"  # required for config.urls namespace


urlpatterns = [
    path("", room_views.list_all_rooms, name="home"),
]
