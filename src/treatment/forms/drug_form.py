from django.forms import ModelForm
from treatment.models.drug_model import Drug


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ["name", "dose", "unit", "dosage_form"]
