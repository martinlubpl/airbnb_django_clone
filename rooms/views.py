from django.views.generic.list import ListView
from django.utils import timezone
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
