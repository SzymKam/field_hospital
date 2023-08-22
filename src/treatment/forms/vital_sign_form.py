from django.forms import ModelForm

from treatment.models.vital_sign_model import VitalSign


class VitalSignForm(ModelForm):
    class Meta:
        model = VitalSign
        fields = ["bp_sys", "bp_dia", "hr", "sao2", "temperature", "glycemia", "gcs"]
