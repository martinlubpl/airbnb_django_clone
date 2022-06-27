import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users.models import User
from rooms.models import Room


class Command(BaseCommand):

    help = "creates list of user favourited houses"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many lists you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(
            List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created_lists = seeder.execute()
        created_lists = flatten(list(created_lists.values()))
        for pk in created_lists:
            list_ = List.objects.get(pk=pk)
            selection = rooms[
                random.randint(0, 20) : random.randint(21, 40)
            ]  # todo: use random.select(rooms, randint)
            list_.room.add(*selection)

        self.stdout.write(self.style.SUCCESS(f"{number} lists created!"))
