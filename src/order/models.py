from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
