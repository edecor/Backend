from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("api/", include("products.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/dj-rest-auth/", include("dj_rest_auth.urls")),
    path("api/dj-rest-auth/registration", include("dj_rest_auth.registration.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("products.urls")),
]

if settings.DEBUG:
    urlpatterns += [
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
    admin.site.site_header = "edecor"
    admin.site.index_title = "Control Room"
    admin.site.site_title = "edecor@live"
