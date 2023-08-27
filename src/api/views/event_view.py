from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.serializers.event_serializer import EventSerializer
from events.models import Event


class EventViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        status = serializer.validated_data.get("status")
        allowed_status = ["Preparing", "In progress"]
        if status not in allowed_status:
            raise ValidationError("Invalid status")
        serializer.save()

    def perform_update(self, serializer):
        if "status" in serializer.validated_data.keys():
            status = serializer.validated_data.get("status")
            allowed_status = ["Preparing", "In progress"]
            if status not in allowed_status:
                raise ValidationError("Invalid status")
        serializer.save()
