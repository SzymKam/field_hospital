from rest_framework import serializers

from treatment.models.treatment_model import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ["patient", "interview", "vital_sign", "drug", "description", "diagnosis", "medical_staff"]
