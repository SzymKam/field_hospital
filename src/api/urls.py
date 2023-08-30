from rest_framework.routers import SimpleRouter

from .views.authorized_person_view import AuthorizedPersonViewSet
from .views.drug_view import DrugViewSet
from .views.event_view import EventViewSet
from .views.medical_staff_view import MedicalStaffViewSet
from .views.patient_view import PatientViewSet
from .views.treatment_view import TreatmentViewSet
from .views.user_view import ChangePasswordUserView, UpdateUserView, UserViewSet
from .views.vital_sign_view import VitalSignViewSet

router = SimpleRouter()
router.register(r"user", UserViewSet, basename="api-user")
router.register(r"user-update", UpdateUserView, basename="api-user-update")
router.register(r"user-password-reset", ChangePasswordUserView, basename="api-user-password-reset")
router.register(r"event", EventViewSet, basename="api-event")
router.register(r"medical-staff", MedicalStaffViewSet, basename="api-medical-staff")
router.register(r"patient", PatientViewSet, basename="api-patient")
router.register(r"authorized-person", AuthorizedPersonViewSet, basename="api-authorized-person")
router.register(r"treatment", TreatmentViewSet, basename="api-treatment")
router.register(r"drug", DrugViewSet, basename="api-drug")
router.register(r"vital-sign", VitalSignViewSet, basename="api-vital-sign")

urlpatterns = router.urls
