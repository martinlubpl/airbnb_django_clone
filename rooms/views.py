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
    s_amenities = request.GET.getlist("amenities")  # get list of pks
    s_facilities = request.GET.getlist("facilities")
    instant = bool(request.GET.get("instant", False))
    # print(instant)
    superhost = bool(request.GET.get("superhost", False))

    chosen = {
        "selected_city": city,
        "selected_country": country,  # chosen
        "selected_room_type": room_type,  # chosen
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
        "s_amenities": s_amenities,
        "s_facilities": s_facilities,
        "instant": instant,
        "superhost": superhost,
    }

    choices = {
        "countries": countries,  # all
        "room_types": room_types,  # all
        "amenities": amenities,
        "facilities": facilities,
    }

    query_filters = {}
    # FIELD LOOKUPS!
    if city != "Anywhere":
        query_filters["city__startswith"] = city
    # print(query_filters)
    # print(country)
    if country != "Anywhere":
        query_filters["country"] = country
    if room_type != 0:
        query_filters["room_type__pk__exact"] = room_type  # fk use pk
    if price > 0:
        query_filters["price__lte"] = price
    if guests > 0:
        query_filters["guests__gte"] = guests
    if bedrooms > 0:
        query_filters["bedrooms__gte"] = bedrooms
    if beds > 0:
        query_filters["beds__gte"] = beds
    if baths > 0:
        query_filters["baths__gte"] = baths
    if instant is True:
        query_filters["instant_book"] = True
    if superhost is True:
        query_filters["host__superhost"] = True
    if len(s_amenities) > 0:
        for a_pk in s_amenities:
            query_filters["amenities__pk"] = int(a_pk)
    if len(s_facilities) > 0:
        for f_pk in s_facilities:
            query_filters["facilities__pk"] = int(f_pk)

    # print(query_filters)
    rooms = models.Room.objects.filter(**query_filters)
    # print(rooms)

    return render(
        request,
        "rooms/search.html",
        context={**chosen, **choices, "rooms": rooms},  # **unpack dict, * for tuples
    )
