from django.forms import ModelForm
from treatment.models.treatment_model import Treatment
from .models.medical_staff_model import MedicalStaff
from .models.drug_model import Drug
from .models.vital_sign_model import VitalSign


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


class UpdateTreatmentMedicalStaffForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "medical_staff",
        ]


class UpdateTreatmentDiagnosisForm(ModelForm):
    class Meta:
        model = Treatment
        fields = [
            "diagnosis",
        ]


class VitalSignForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = "__all__"


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ["name", "dose", "unit", "dosage_form"]


class MedicalStaffForm(ModelForm):
    class Meta:
        model = MedicalStaff
        fields = "__all__"
