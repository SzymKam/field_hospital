from django.forms import ModelForm
from .models import Patient, AuthorizedPerson


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"


class AuthorizedPersonForm(ModelForm):
    class Meta:
        model = AuthorizedPerson
        fields = "__all__"
