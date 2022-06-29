# from django.shortcuts import render
# from django.http import HttpResponse
# import math

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from . import models


# Create your views here.


def list_all_rooms(request):

    page = int(request.GET.get("page", 1) or 1)
    room_list = models.Room.objects.all()  # lazy
    paginator = Paginator(
        room_list,
        per_page=10,
        orphans=5,
    )  # attach 5 or less orphans to previous page
    # rooms = paginator.get_page(page)

    # with page() you can catch exceptions
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/list_all_rooms.html",
            context={
                "page": rooms,
            },
        )
    except EmptyPage:
        # rooms = paginator.page(1)
        return redirect("/")
