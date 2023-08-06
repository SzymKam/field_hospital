from django.urls import path

from .views.treatment_views import CreateTreatmentView, DetailTreatmentView


urlpatterns = [
    path(
        "events/<int:event>/patients/<int:patient>/treatment/create",
        CreateTreatmentView.as_view(),
        name="create-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>",
        DetailTreatmentView.as_view(),
        name="detail-treatment",
    ),
]
