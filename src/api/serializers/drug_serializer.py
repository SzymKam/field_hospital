from rest_framework import serializers

from treatment.models.drug_model import Drug


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ["name", "dose", "unit", "dosage_form", "treatment", "id"]
