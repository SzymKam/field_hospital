from django.forms import ModelForm
from treatment.models.treatment_model import Treatment
from treatment.models.medical_staff_model import MedicalStaff


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


class UpdateTreatmentDescriptionForm(ModelForm):
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
