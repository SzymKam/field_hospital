from django.urls import path

from .views import (
    AllActiveEventView,
    AllInactiveEventView,
    CreateEventView,
    DetailEventView,
    UpdateEventView,
    DeleteEventView,
)

urlpatterns = [
    path("", AllActiveEventView.as_view(), name="all-events"),
    path("create-event/", CreateEventView.as_view(), name="add-events"),
    path("detail-event/<int:pk>", DetailEventView.as_view(), name="detail-events"),
    path("update-event/<int:pk>", UpdateEventView.as_view(), name="update-events"),
    path("inactive-event/", AllInactiveEventView.as_view(), name="complete-events"),
    path("delete-events/<int:pk>", DeleteEventView.as_view(), name="delete-events"),
]
