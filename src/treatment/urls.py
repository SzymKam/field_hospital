from django.urls import path

from .views.treatment_views import (
    CreateTreatmentView,
    DetailTreatmentView,
    UpdateTreatmentInterviewView,
    UpdateTreatmentDescriptionView,
    UpdateTreatmentMedicalStaffView,
    UpdateTreatmentDiagnosisView,
)
from .views.drug_views import CreateDrugView, UpdateDrugView, DeleteDrugView
from .views.vital_sign_view import CreateVitalSignView

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
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:treatment>/drug/<int:pk>",
        UpdateDrugView.as_view(),
        name="edit-drug-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:treatment>/drug/<int:pk>/delete",
        DeleteDrugView.as_view(),
        name="delete-drug-treatment",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/treatment/<int:pk>/vital-sign",
        CreateVitalSignView.as_view(),
        name="vital-sign-treatment",
    ),
]
