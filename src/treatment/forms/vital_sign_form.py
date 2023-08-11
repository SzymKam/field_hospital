from treatment.models.vital_sign_model import VitalSign
from django.forms import ModelForm


class VitalSignForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = ["name", "value"]
