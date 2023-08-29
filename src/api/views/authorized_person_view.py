from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.authorized_person_serializer import AuthorizedPersonSerializer
from patients.models import AuthorizedPerson


class AuthorizedPersonViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AuthorizedPersonSerializer
    queryset = AuthorizedPerson.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        patient = self.request.query_params.get("patient")
        if patient:
            queryset = queryset.filter(patient=patient)
        return queryset
