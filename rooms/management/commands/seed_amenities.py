from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "help my command"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many times",
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Wifi",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Pool",
            "Hot tub",
            "Free parking on premises",
            "EV charger",
            "Crib",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]

        for amenity in amenities:
            Amenity.objects.create(name=amenity)

        self.stdout.write(self.style.SUCCESS("Amenities created"))

        # times = options.get("times")
        # for t in range(int(times)):
        #     self.stdout.write(self.style.ERROR("test3"))
