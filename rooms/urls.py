from django.urls import path

from .views import RoomDetailView

urlpatterns = [
    path("<name>/", RoomDetailView.as_view(), name="room-detail"),
]
