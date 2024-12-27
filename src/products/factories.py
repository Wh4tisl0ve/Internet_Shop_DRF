import factory.django, random

from factory import Faker

from categories.factories import CategoryFactory

from products.models import Product



class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = Faker("word")
    description = Faker("text")
    price = factory.LazyFunction(lambda: round(random.uniform(1.0, 100.0), 2))
    characteristics = Faker("sentence")
    image = factory.django.ImageField(color="blue")
    category = factory.SubFactory(CategoryFactory)
