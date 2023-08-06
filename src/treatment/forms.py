from django.forms import ModelForm
from .models import Treatment, VitalSign, Drug, MedicalStaff


class CreateTreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "medical_staff",
        ]


class UpdateTreatmentInterviewForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "interview",
        ]


class UpdateDescriptionInterviewForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "description",
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
