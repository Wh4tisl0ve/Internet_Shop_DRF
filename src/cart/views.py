from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import CartItem
from .serializers import CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_cart(self):
        return self.request.user.cart

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.get_cart())

    def perform_create(self, serializer):
        serializer.save(cart=self.get_cart())
