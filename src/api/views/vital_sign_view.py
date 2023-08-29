from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.vital_sign_serializer import VitalSignSerializer
from treatment.models.vital_sign_model import VitalSign


class VitalSignViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = VitalSignSerializer
    queryset = VitalSign.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        treatment = self.request.query_params.get("treatment")
        if treatment:
            queryset = queryset.filter(treatment=treatment)
        return queryset
