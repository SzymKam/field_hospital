from django.forms import ModelForm
from .models import Treatment, VitalSign, Drug, MedicalStaff


class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = "__all__"


class CreateTreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "medical_staff",
        ]


class VitalSignForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = "__all__"


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = "__all__"


class MedicalStaffForm(ModelForm):
    class Meta:
        model = MedicalStaff
        fields = "__all__"
