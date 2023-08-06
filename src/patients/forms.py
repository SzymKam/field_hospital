from django.forms import ModelForm
from .models import Patient, AuthorizedPerson
from django.forms.widgets import DateInput, DateTimeInput
from datetime import datetime


class PatientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.initial_form_data = f"NN {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}"
        if "initial" not in kwargs:
            kwargs["initial"] = {}
        if "surname" not in kwargs["initial"]:
            kwargs["initial"]["surname"] = self.initial_form_data

        super().__init__(*args, **kwargs)
        self.fields["event"].widget.attrs["disabled"] = True

    def save(self, commit=True):
        instance = super(PatientForm, self).save(commit=False)
        if instance.surname == "":
            instance.surname = self.initial_form_data

        if commit:
            instance.save()

        return instance

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
