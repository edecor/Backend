from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path("api/products/", include("products.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration", include("dj_rest_auth.registration.urls")),
    path("", include("products.urls")),
    path("accounts/", include("allauth.urls")),
    path("api/profile/", include("user_profiles.urls")),
    path("api/rooms/", include("rooms.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path("admin/", admin.site.urls),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
    admin.site.site_header = "127.0.0.1"
    admin.site.index_title = "Switchboard"
    admin.site.site_title = "edecor@localhost"

if not settings.DEBUG:
    urlpatterns += [
        path("orEifasjfasdfaslas/", admin.site.urls),
    ]
    admin.site.site_header = "edecor Control Room"
    admin.site.index_title = "Control Room"
    admin.site.site_title = "edecor@live"
