import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms.models import Room, RoomType, Photo
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
        created_rooms = seeder.execute()
        created_rooms = flatten(list(created_rooms.values()))

        for pk in created_rooms:
            room = Room.objects.get(pk=pk)
            for i in range(random.randint(3, 15)):
                Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"/room_photos/{random.randint(1,111)}.jpg",
                    room=room,
                )

        self.stdout.write(self.style.SUCCESS(f"{number} rooms created"))
