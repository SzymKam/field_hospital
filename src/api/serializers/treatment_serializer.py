from rest_framework import serializers

from patients.models import Patient
from treatment.models.treatment_model import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ["id", "patient", "interview", "vital_sign", "drug", "description", "diagnosis", "medical_staff"]
