from django.urls import path
from django.http import HttpResponse

from .views import CustomerProfileDetailView, WishListDetailView, CommentListView


def testview(request):
    return HttpResponse("hi")


urlpatterns = [
    path("comments/", CommentListView.as_view(), name="comment_list"),
    path(
        "<uuid>/", CustomerProfileDetailView.as_view(), name="customer_profile_detail"
    ),
    path("wishes/<id>/", WishListDetailView.as_view(), name="wishlist_detail"),
]
