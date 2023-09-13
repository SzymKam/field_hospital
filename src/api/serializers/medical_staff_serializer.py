from rest_framework import serializers

from treatment.models.medical_staff_model import MedicalStaff


class MedicalStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalStaff
        fields = "__all__"
