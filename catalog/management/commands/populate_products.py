from django.core.management.base import BaseCommand
from catalog.models import Product
from faker import Faker
import random


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--count', type=int, default=30, help='Сколько создать')

    def handle(self, *args, **options):
        fake = Faker('ru_RU')
        count = options['count']
        created = 0

        for _ in range(count):
            name = fake.word().capitalize() + " " + fake.word()
            price = round(random.uniform(500, 10000), 2)
            quantity = random.randint(0, 100)

            Product.objects.create(
                name=name,
                price=price,
                quantity=quantity,
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Создано: {created}'))
