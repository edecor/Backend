from django.urls import path

from .views import CustomerProfileDetailView, WishListDetailView, CommentListView

urlpatterns = [
    path("comments/", CommentListView.as_view(), name="comment_list"),
    path(
        "<uuid>/", CustomerProfileDetailView.as_view(), name="customer_profile_detail"
    ),
    path("wishes/<id>/", WishListDetailView.as_view(), name="wishlist_detail"),
]
