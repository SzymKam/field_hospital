from django.urls import path

from .views.treatment_views import (
    CreateTreatmentView,
    DetailTreatmentView,
    UpdateTreatmentInterviewView,
    UpdateTreatmentDescriptionView,
    UpdateTreatmentMedicalStaffView,
    UpdateTreatmentDiagnosisView,
    CreateDrugView,
)


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
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/interview",
        UpdateTreatmentInterviewView.as_view(),
        name="interview-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/description",
        UpdateTreatmentDescriptionView.as_view(),
        name="description-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/medical-staff",
        UpdateTreatmentMedicalStaffView.as_view(),
        name="medical-staff-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/diagnosis",
        UpdateTreatmentDiagnosisView.as_view(),
        name="diagnosis-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/drug",
        CreateDrugView.as_view(),
        name="drug-treatment",
    ),
]
