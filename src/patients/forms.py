from django.forms import ModelForm
from .models import Patient, AuthorizedPerson
from django.forms.widgets import DateInput, DateTimeInput


class PatientForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['event'].widget.attrs['disabled'] = True

    class Meta:
        widgets = {
            "birth_date": DateInput(attrs={"type": "date"}),
            "admission_date": DateTimeInput(attrs={"type": "datetime-local"}),
        }
        model = Patient
        exclude = (
            "authorized_person",
            "treatment",
        )


class DetailPatientForm(ModelForm):
    class Meta:
        widgets = {
            "birth_date": DateInput(attrs={"type": "date"}),
            "admission_date": DateTimeInput(attrs={"type": "datetime-local"}),
        }
        model = Patient
        exclude = ("status", "event", "treatment", "authorized_person")


class AuthorizedPersonForm(ModelForm):
    class Meta:
        model = AuthorizedPerson
        fields = "__all__"
