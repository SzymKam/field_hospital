import datetime

from rest_framework import serializers

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def to_representation(self, instance):
        start_date = instance.start_date
        if isinstance(start_date, datetime.datetime):
            converted_start_date = start_date.date()
            instance.start_date = converted_start_date

        data = super().to_representation(instance)

        return data
