import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room, RoomType
from users.models import User


class Command(BaseCommand):
    help = "creates rooms in db from array"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help="how many rooms",
            default=1,
            type=int,  # auto convert
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()  # dont do it on big user db (choose first 50 ex)
        room_types = RoomType.objects.all()
        seeder.add_entity(
            Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(room_types),
                "price": lambda x: random.randint(100, 500),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 3),
                "baths": lambda x: random.randint(1, 3),
                "guests": lambda x: random.randint(1, 6),
                "name": lambda x: seeder.faker.address(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
