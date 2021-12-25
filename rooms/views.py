from django.shortcuts import render
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "name"
