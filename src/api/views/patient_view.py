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
