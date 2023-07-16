from django.urls import path

from .views import AllEventView, CreateEventView, DetailEventView

urlpatterns = [
    path("", AllEventView.as_view(), name="all-events"),
    path("create-event/", CreateEventView.as_view(), name="add-events"),
    path("detail-event/<int:pk>", DetailEventView.as_view(), name="detail-events"),
]
