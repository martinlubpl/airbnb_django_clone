# from django.shortcuts import render
# from django.http import HttpResponse
# import math
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.


def list_all_rooms(request):

    page = int(request.GET.get("page", 1) or 1)
    # page_size = 10
    # all_rooms = models.Room.objects.all()[(page - 1) * page_size : page * page_size]
    # page_count = math.ceil(models.Room.objects.count() // page_size) + 1
    room_list = models.Room.objects.all()  # lazy
    paginator = Paginator(
        room_list,
        per_page=10,
        orphans=5,
    )  # attach 5 or less orphans to previous page
    # rooms = paginator.get_page(page)
    rooms = paginator.page(int(page))
    print(dir(rooms))
    return render(
        request,
        "rooms/list_all_rooms.html",
        context={
            "page": rooms,
            #     "page": page,
            #     "page_count": page_count,
            #     "page_range": range(1, page_count + 1),
        },
    )
