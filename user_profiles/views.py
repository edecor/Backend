from rest_framework import generics

from .models import Customer, WishList
from .serializers import CustomerProfileSerializer, WishListSerializer


class CustomerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    lookup_field = "uuid"


class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    lookup_field = "id"
