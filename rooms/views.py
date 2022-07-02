from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.utils import timezone


from django.shortcuts import render

# from django.urls import reverse
# from django.http import Http404


# from django_countries import countries
from . import models, forms


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


class SearchView(View):
    def get(self, request):
        # if no country return empty to render without error complains
        country = request.GET.get("country")
        if country:
            form = forms.SearchForm(request.GET)  # r.GET to remember values
            if form.is_valid():  # True if no errors
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                room_type = form.cleaned_data.get("room_type")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                query_filters = {}
                # FIELD LOOKUPS!
                if city != "Anywhere":
                    query_filters["city__startswith"] = city
                # print(query_filters)
                # print(country)
                if country != "Anywhere":
                    query_filters["country"] = country
                if room_type is not None:
                    query_filters["room_type"] = room_type  # fk use pk
                if price is not None:
                    query_filters["price__lte"] = price
                if guests is not None:
                    query_filters["guests__gte"] = guests
                if bedrooms is not None:
                    query_filters["bedrooms__gte"] = bedrooms
                if beds is not None:
                    query_filters["beds__gte"] = beds
                if baths is not None:
                    query_filters["baths__gte"] = baths
                if instant_book is True:
                    query_filters["instant_book"] = True
                if superhost is True:
                    query_filters["host__superhost"] = True

                for a in amenities:
                    query_filters["amenities"] = a

                for f in facilities:
                    query_filters["facilities"] = f

                rooms = models.Room.objects.filter(**query_filters)

        else:
            form = forms.SearchForm()

        return render(
            request,
            "rooms/search.html",
            context={
                "form": form,
                "rooms": rooms,
            },
        )
