from rest_framework import generics

from catalog.models import Product
from catalog.serializers import ProductSerializer


class CatalogView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
