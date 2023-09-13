from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.medical_staff_serializer import MedicalStaffSerializer
from treatment.models.medical_staff_model import MedicalStaff

from ..constants import ALLOWED_MEDICAL_QUALIFICATIONS


class MedicalStaffViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MedicalStaffSerializer
    queryset = MedicalStaff.objects.all()

    def perform_create(self, serializer):
        medical_qualifications = serializer.validated_data.get("medical_qualifications")
        allowed_medical_qualifications = ALLOWED_MEDICAL_QUALIFICATIONS
        if medical_qualifications not in allowed_medical_qualifications:
            raise ValidationError("Invalid medical qualifications")
        serializer.save()

    def perform_update(self, serializer):
        if "medical_qualifications" in serializer.validated_data.keys():
            medical_qualifications = serializer.validated_data.get("medical_qualifications")
            allowed_medical_qualifications = ALLOWED_MEDICAL_QUALIFICATIONS
            if medical_qualifications not in allowed_medical_qualifications:
                raise ValidationError("Invalid medical qualifications")
        serializer.save()
