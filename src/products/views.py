from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        return self.serializer_class
