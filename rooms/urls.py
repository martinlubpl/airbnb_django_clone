from django.urls import path
from . import views

app_name = "rooms"  # namespace

urlpatterns = [
    path("<int:pk>", views.RoomDetail.as_view(), name="room_detail"),
]
