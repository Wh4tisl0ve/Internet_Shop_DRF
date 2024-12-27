from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import CartItem, Cart

from .models import Order, OrderItem
from .serializers import OrderItemSerializer


class CreateOrderView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart_items = CartItem.objects.filter(cart=self.request.user.cart)

        order = Order.objects.create(user=request.user, status="Выполнен")

        order_items = [
            OrderItem(order=order, product=item.product, quantity=item.quantity)
            for item in cart_items
        ]

        OrderItem.objects.bulk_create(order_items)
        cart_items.delete()

        order_items = OrderItemSerializer(order.items.all(), many=True)

        return Response(
            {"order": {"id": order.id, "items": order_items.data}},
            status=201,
        )
