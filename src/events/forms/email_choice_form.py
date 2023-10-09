from django import forms
from django.contrib.auth.models import User


class EmailChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.username} - {obj.first_name} {obj.last_name} - {obj.email}"


class EmailSelectionForm(forms.Form):
    email = EmailChoiceField(
        queryset=User.objects.all(),
        empty_label="Select an email",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
