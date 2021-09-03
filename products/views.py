from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-id"]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]
