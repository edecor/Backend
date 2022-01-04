from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Customer, WishList, Comment
from .serializers import (
    CustomerProfileSerializer,
    WishListSerializer,
    CommentSerializer,
)


class CustomerProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer
    lookup_field = "uuid"


class WishListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    lookup_field = "id"


class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
