from django.urls import path
from .views import CreatePatientView

urlpatterns = [
    path("<int:event>/add-patient", CreatePatientView.as_view(), name="add-patient"),
]
