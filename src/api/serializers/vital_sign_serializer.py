from rest_framework import serializers

from treatment.models.vital_sign_model import VitalSign


class VitalSignSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSign
        fields = "__all__"
