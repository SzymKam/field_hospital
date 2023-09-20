from django.db import models
from django.utils import timezone

from events.models import Event
from treatment.models.treatment_model import Treatment

from .constants import BED_CHOICE, PRIORITY_CHOICE


class AuthorizedPerson(models.Model):
    name = models.CharField(max_length=50, help_text="Person name")
    surname = models.CharField(max_length=50, help_text="Person surname")
    phone = models.IntegerField(blank=True, null=True, help_text="Person phone number")


class Patient(models.Model):
    admission_date = models.DateTimeField(help_text="Date of patient admission", default=timezone.now)
    name = models.CharField(max_length=50, help_text="Patient name", blank=True)
    surname = models.CharField(max_length=50, help_text="Patient surname", blank=True)
    priority = models.CharField(choices=PRIORITY_CHOICE, help_text="Priority", blank=True, null=True)
    PESEL = models.IntegerField(blank=True, null=True, help_text="Patient PESEL number")
    birth_date = models.DateField(blank=True, null=True, help_text="Patient birth date")
    address = models.CharField(blank=True, help_text="Patient address", max_length=100)
    phone = models.IntegerField(blank=True, null=True, help_text="Patient phone number")
    email = models.EmailField(blank=True, null=True, help_text="Patient e-mail")
    additional_info = models.TextField(blank=True, help_text="Additional info about patient")
    bed_number = models.CharField(
        choices=BED_CHOICE,
        blank=True,
        help_text="Bed number in hospital",
        max_length=6,
        default="No bed",
    )
    authorized_person = models.OneToOneField(
        AuthorizedPerson,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Set authorized person",
        related_name="patient",
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        help_text="Set event",
        related_name="patient",
    )
    treatment = models.OneToOneField(
        Treatment,
        on_delete=models.CASCADE,
        help_text="Add treatment",
        related_name="patient",
        blank=True,
        null=True,
    )
    status = models.CharField(default="Active", max_length=20)

    def __str__(self):
        return f"{self.name} - {self.id}"
