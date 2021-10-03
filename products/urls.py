from django.urls import path
from .views import ProductListView, ProductDetailView, tempOKview, trigger_error

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<slug>", ProductDetailView.as_view(), name="product-detail"),
    path("", tempOKview),
    path("sentry-debug/", trigger_error),
]
