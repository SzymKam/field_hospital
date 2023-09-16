from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    AllActiveEventView,
    AllInactiveEventView,
    CloseRestoreEventView,
    CreateEventView,
    DeleteEventView,
    DetailEventView,
    UpdateEventView,
)

urlpatterns = (
    [
        path("", AllActiveEventView.as_view(), name="all-events"),
        path("events/", CreateEventView.as_view(), name="add-events"),
        path("events/<int:pk>", DetailEventView.as_view(), name="detail-events"),
        path("events/<int:pk>/update", UpdateEventView.as_view(), name="update-events"),
        path("events/inactive/", AllInactiveEventView.as_view(), name="complete-events"),
        path("events/<int:pk>/delete", DeleteEventView.as_view(), name="delete-events"),
        path("events/<int:pk>/close", CloseRestoreEventView.close_event, name="close-events"),
        path(
            "events/<int:pk>/restore",
            CloseRestoreEventView.restore_event,
            name="restore-events",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
