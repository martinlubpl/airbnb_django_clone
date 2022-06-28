# from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.


def list_all_rooms(request):
    all_rooms = models.Room.objects.all()

    return render(
        request,
        "rooms/list_all_rooms.html",
        context={
            "rooms": all_rooms,
        },
    )
