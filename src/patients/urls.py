from django.urls import path
from patients.views.patients_views import (
    CreatePatientView,
    DetailPatientView,
    UpdatePatientView,
    DischargePatientView,
)
from patients.views.auth_person_view import CreateAuthPersonView

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
        "event/<int:event>/patients/<int:pk>/discharge",
        DischargePatientView.discharge_patient,
        name="discharge-patient",
    ),
    path(
        "event/<int:event>/patients/<int:pk>/add-auth-person",
        CreateAuthPersonView.as_view(),
        name="add-auth-person",
    ),
]
