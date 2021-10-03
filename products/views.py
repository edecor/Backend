from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponse


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-updated"]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]


def tempOKview(request):
    return HttpResponse("hi")


def trigger_error(request):
    division_by_zero = 1 / 0
