from django.urls import path
from .views import CreatePatientView, DetailPatientView

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
]
