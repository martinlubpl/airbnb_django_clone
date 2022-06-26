from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = "creates users in db with django_seed"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            help="how many users",
            default=1,
            type=int,  # auto convert
        )

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        num = int(options.get("number"))

        seeder.add_entity(
            User,
            num,
            {
                "is_staff": False,
                "is_superuser": False,
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{num} USers created "))
