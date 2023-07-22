from django.urls import path
from .views import (
    CreatePatientView,
    DetailPatientView,
    UpdatePatientView,
    DischargePatientView,
)

urlpatterns = [
    path(
        "event:<int:event>/add-patient",
        CreatePatientView.create_patient,
        name="add-patient",
    ),
    path(
        "event:<int:event>/patient:<int:pk>",
        DetailPatientView.as_view(),
        name="detail-patient",
    ),
    path(
        "event:<int:event>/patient:<int:pk>/update",
        UpdatePatientView.as_view(),
        name="update-patient",
    ),
    path(
        "event:<int:event>/patient:<int:pk>/discharge",
        DischargePatientView.discharge_patient,
        name="discharge-patient",
    ),
]
