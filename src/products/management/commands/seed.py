import random

from django.core.management.base import BaseCommand

from products.factories import ProductFactory
from categories.factories import CategoryFactory


class Command(BaseCommand):
    help = "Seeds the database with categories and products."

    def add_arguments(self, parser):
        parser.add_argument(
            "--categories",
            default=10,
            type=int,
            help="The number of categories to create.",
        )
        parser.add_argument(
            "--products",
            default=200,
            type=int,
            help="The number of fake products to create.",
        )

    def handle(self, *args, **options):
        categories = [CategoryFactory.create() for _ in range(options["categories"])]
        for _ in range(options["products"]):
            ProductFactory.create(category=random.choice(categories))
