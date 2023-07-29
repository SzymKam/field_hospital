from django.urls import path
from .views import (
    CreatePatientView,
    DetailPatientView,
    UpdatePatientView,
    DischargePatientView,
)

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
]
