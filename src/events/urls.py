from django.urls import path

from .views import (
    AllActiveEventView,
    AllInactiveEventView,
    CreateEventView,
    DetailEventView,
    UpdateEventView,
    DeleteEventView,
    CloseRestoreEventView,
)

urlpatterns = [
    path("", AllActiveEventView.as_view(), name="all-events"),
    path("add-event/", CreateEventView.as_view(), name="add-events"),
    path("detail-event/<int:pk>", DetailEventView.as_view(), name="detail-events"),
    path("update-event/<int:pk>", UpdateEventView.as_view(), name="update-events"),
    path("inactive-event/", AllInactiveEventView.as_view(), name="complete-events"),
    path("delete-event/<int:pk>", DeleteEventView.as_view(), name="delete-events"),
    path(
        "close-event/<int:pk>", CloseRestoreEventView.close_event, name="close-events"
    ),
    path(
        "restore-event/<int:pk>",
        CloseRestoreEventView.restore_event,
        name="restore-events",
    ),
]
