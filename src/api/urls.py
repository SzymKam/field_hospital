from rest_framework.routers import SimpleRouter

from .views.event_view import EventViewSet
from .views.medical_staff_view import MedicalStaffViewSet
from .views.patient_view import PatientViewSet
from .views.user_view import UserViewSet

router = SimpleRouter()
router.register(r"user", UserViewSet, basename="api-user")
router.register(r"event", EventViewSet, basename="api-event")
router.register(r"medical-staff", MedicalStaffViewSet, basename="api-medical-staff")
router.register(r"patient", PatientViewSet, basename="api-patient")


urlpatterns = [] + router.urls
