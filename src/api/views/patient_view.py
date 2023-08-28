from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.patient_serializer import PatientSerializer
from patients.models import Patient


class PatientViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        event = self.request.query_params.get("event")
        if event:
            queryset = queryset.filter(event=event)
        return queryset
