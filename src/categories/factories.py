import factory.django

from factory import Faker

from .models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = Faker("word")
