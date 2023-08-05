from django.urls import path
from patients.views.patients_views import (
    CreatePatientView,
    DetailPatientView,
    UpdatePatientView,
    DischargePatientView,
)
from patients.views.auth_person_view import CreateAuthPersonView, UpdateAuthPersonView

urlpatterns = [
    path(
        "events/<int:event>/patients",
        CreatePatientView.create_patient,
        name="add-patient",
    ),
    path(
        "events/<int:event>/patients/<int:pk>",
        DetailPatientView.as_view(),
        name="detail-patient",
    ),
    path(
        "events/<int:event>/patients/<int:pk>/update",
        UpdatePatientView.as_view(),
        name="update-patient",
    ),
    path(
        "events/<int:event>/patients/<int:pk>/discharge",
        DischargePatientView.discharge_patient,
        name="discharge-patient",
    ),
    path(
        "events/<int:event>/patients/<int:pk>/auth-person",
        CreateAuthPersonView.as_view(),
        name="add-auth-person",
    ),
    path(
        "events/<int:event>/patients/<int:patient>/auth-person/<int:pk>/update",
        UpdateAuthPersonView.as_view(),
        name="update-auth-person",
    ),
]
