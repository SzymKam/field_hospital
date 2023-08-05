from django.urls import path

from .views import CreateTreatmentView


urlpatterns = [
    path("treatment/", CreateTreatmentView.as_view(), name="treatment"),
]
