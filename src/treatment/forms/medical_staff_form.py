from django.forms import ModelForm
from treatment.models.medical_staff_model import MedicalStaff


class MedicalStaffForm(ModelForm):
    class Meta:
        model = MedicalStaff
        fields = "__all__"
