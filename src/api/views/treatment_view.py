from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.treatment_serializer import TreatmentSerializer
from treatment.models.treatment_model import Treatment


class TreatmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        patient = self.request.query_params.get("patient")
        if patient:
            queryset = queryset.filter(patient=patient)
        return queryset
