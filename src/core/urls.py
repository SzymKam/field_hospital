from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .env import env

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    path("", include("patients.urls")),
    path("", include("treatment.urls")),
    path("users/", include("users.urls")),
    path("api/", include("api.urls")),
]

if env("DEBUG"):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
