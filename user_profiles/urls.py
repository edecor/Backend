from django.urls import path

from .views import CustomerProfileDetailView

urlpatterns = [
    path("<id>/", CustomerProfileDetailView.as_view(), name="customer_profile_detail"),
]
