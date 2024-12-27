from django.db import models

from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="products/images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    characteristics = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
