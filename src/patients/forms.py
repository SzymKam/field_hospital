from django.forms import ModelForm
from .models import Patient, AuthorizedPerson
from django.forms.widgets import DateInput


class PatientForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['event'].widget.attrs['disabled'] = True

    class Meta:
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        model = Patient
        exclude = (
            "authorized_person",
            "treatment",
        )


class DetailPatientForm(ModelForm):
    class Meta:
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        model = Patient
        exclude = (
            "status",
            "event",
        )


class AuthorizedPersonForm(ModelForm):
    class Meta:
        model = AuthorizedPerson
        fields = "__all__"
