from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        widgets = {"start_date": DateInput(attrs={"type": "date"})}
        model = Event
        fields = ["name", "start_date", "description", "localization", "status"]


class CloseEventForm(ModelForm):
    class Meta:
        widgets = {"end_date": DateInput(attrs={"type": "date"})}
        model = Event
        fields = ["end_date"]
