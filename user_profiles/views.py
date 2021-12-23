from rest_framework import generics
from rest_framework.serializers import Serializer

from .models import Customer
from .serializers import CustomerProfileSerializer


class CustomerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    lookup_field = "uuid"
