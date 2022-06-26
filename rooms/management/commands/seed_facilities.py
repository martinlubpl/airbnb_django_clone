from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = "creates facilities in db from array"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="how many times",
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for facility in facilities:
            Facility.objects.create(name=facility)

        self.stdout.write(self.style.SUCCESS("Facilities created"))

        # times = options.get("times")
        # for t in range(int(times)):
        #     self.stdout.write(self.style.ERROR("test3"))
