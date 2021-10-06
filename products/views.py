from .serializers import MaterialSerializer
from .models import Material
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import HttpResponse


class MaterialListView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filter_backends = [filters.OrderingFilter]
    ordering = ["-updated"]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer()
    lookup_field = "slug"
    permission_classes = [IsAuthenticatedOrReadOnly]


def tempOKview(request):
    return HttpResponse("hi")


def trigger_error(request):
    division_by_zero = 1 / 0
