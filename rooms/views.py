from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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


def search(request):
    form = forms.SearchForm()

    return render(request, "rooms/search.html", context={"form": form})
