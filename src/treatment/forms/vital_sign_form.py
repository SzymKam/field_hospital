from django.forms import ModelForm

from treatment.models.vital_sign_model import VitalSign


class VitalSignForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = ["name", "value", "extra_value"]
