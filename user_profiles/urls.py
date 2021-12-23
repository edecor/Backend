from django.urls import path

from .views import CustomerProfileDetailView, WishListDetailView

urlpatterns = [
    path(
        "<uuid>/", CustomerProfileDetailView.as_view(), name="customer_profile_detail"
    ),
    path("wishes/<id>/", WishListDetailView.as_view(), name="wishlist_detail"),
]
