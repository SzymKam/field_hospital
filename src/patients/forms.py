from django.forms import ModelForm
from .models import Patient, AuthorizedPerson
from django.forms.widgets import DateInput


class PatientForm(ModelForm):
    class Meta:
        widgets = {"birth_date": DateInput(attrs={"type": "date"})}
        model = Patient
        exclude = ("authorized_person", "treatment")


class AuthorizedPersonForm(ModelForm):
    class Meta:
        model = AuthorizedPerson
        fields = "__all__"
