from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.drug_serializer import DrugSerializer
from treatment.models.drug_model import Drug


class DrugViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        treatment = self.request.query_params.get("treatment")
        if treatment:
            queryset = queryset.filter(treatment=treatment)
        return queryset
