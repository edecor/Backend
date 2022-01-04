from django.urls import path

from .views import RoomDetailView, TopRoomsInHome

urlpatterns = [
    path("<name>/", RoomDetailView.as_view(), name="room-detail"),
    path("<name>/home/", TopRoomsInHome.as_view(), name="top-rooms"),
]
