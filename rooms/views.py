from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone


from django.shortcuts import render

# from django.urls import reverse
# from django.http import Http404


from django_countries import countries
from . import models


# Create your views here.


class HomeView(ListView):

    """Home view for index page"""

    template_name = "rooms/room_list.html"
    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    page_kwarg = "page"  # /?page_kwarg=1
    context_object_name = "rooms"
    # page_obj is sent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # additional
        context["time"] = timezone.now()
        return context


class RoomDetail(DetailView):

    """CBV Room Detail"""

    template_name = "rooms/room_detail.html"
    context_object_name = "room"


def search(request):
    # print(vars(request))
    city = (request.GET.get("city", "Anywhere")).capitalize()
    country = request.GET.get("country", "Anywhere")
    room_type = int(request.GET.get("room_type", 0))
    # print(city)
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()
    # house_rules = models.HouseRule.objects.all()

    price = int(request.GET.get("price", 0))
    guests = int(request.GET.get("guests", 0))
    bedrooms = int(request.GET.get("bedrooms", 0))
    beds = int(request.GET.get("beds", 0))
    baths = int(request.GET.get("baths", 0))
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")

    chosen = {
        "selected_city": city,
        "selected_country": country,  # chosen
        "selected_room_type": room_type,  # chosen
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }

    choices = {
        "countries": countries,  # all
        "room_types": room_types,  # all
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(
        request,
        "rooms/search.html",
        context={**chosen, **choices},  # **unpack dict, * for tuples
    )
