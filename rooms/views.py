# from django.shortcuts import render
# from django.http import HttpResponse
import math
from django.shortcuts import render
from . import models


# Create your views here.


def list_all_rooms(request):
    page_size = 10
    page = int(request.GET.get("page", 1) or 1)
    all_rooms = models.Room.objects.all()[(page - 1) * page_size : page * page_size]
    page_count = math.ceil(models.Room.objects.count() // page_size) + 1

    return render(
        request,
        "rooms/list_all_rooms.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
