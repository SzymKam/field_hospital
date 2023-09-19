from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.patient_serializer import PatientSerializer
from patients.models import Patient

from ..constants import ALLOWED_BED_CHOICE, ALLOWED_PRIORITY_CHOICE


class PatientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        event = self.request.query_params.get("event")
        if event:
            queryset = queryset.filter(event=event)
        return queryset

    def perform_create(self, serializer):
        bed_number = serializer.validated_data.get("bed_number")
        priority = serializer.validated_data.get("priority")
        allowed_bed_number = ALLOWED_BED_CHOICE
        allowed_priority = ALLOWED_PRIORITY_CHOICE
        if bed_number not in allowed_bed_number:
            raise ValueError("Invalid bed number")
        if priority not in allowed_priority:
            raise ValueError("Invalid priority")
        serializer.save()

    def perform_update(self, serializer):
        if "bed_number" in serializer.validated_data.keys():
            bed_number = serializer.validated_data.get("bed_number")
            allowed_bed_number = ALLOWED_BED_CHOICE
            if bed_number not in allowed_bed_number:
                raise ValidationError("Invalid bed number choice")
        if "priority" in serializer.validated_data.keys():
            priority = serializer.validated_data.get("priority")
            allowed_priority = ALLOWED_PRIORITY_CHOICE
            if priority not in allowed_priority:
                raise ValidationError("Invalid priority choice")
        serializer.save()
