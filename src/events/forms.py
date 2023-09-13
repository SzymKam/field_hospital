from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import Event


class EventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        excluded_choice = "Ended"
        if excluded_choice in dict(self.fields["status"].choices):
            choices = list(self.fields["status"].choices)
            choices.remove((excluded_choice, excluded_choice))
            self.fields["status"].choices = choices

    class Meta:
        widgets = {"start_date": DateInput(attrs={"type": "date"})}
        model = Event
        fields = ["name", "start_date", "description", "localization", "status"]


class CloseEventForm(ModelForm):
    class Meta:
        widgets = {"end_date": DateInput(attrs={"type": "date"})}
        model = Event
        fields = ["end_date"]
