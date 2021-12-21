from django.urls import path

from .views import MaterialListView, MaterialDetailView, tempOKview, trigger_error
from .views import tempOKview, trigger_error

urlpatterns = [
    path("materials/", MaterialListView.as_view(), name="product-list"),
    path("materials/<slug>/", MaterialDetailView.as_view(), name="product-detail"),
    path("", tempOKview),
    path("sentry-debug/", trigger_error),
]
