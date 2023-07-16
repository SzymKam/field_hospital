from django.db import models

from events.models import Event
from treatment.models import Treatment
from .constants import SEX, BED_CHOICE


class AuthorizedPerson(models.Model):
    name = models.CharField(max_length=50, blank=True, help_text="Person name")
    surname = models.CharField(max_length=50, blank=True, help_text="Person surname")
    phone = models.IntegerField(blank=True, null=True, help_text="Person phone number")


class Patient(models.Model):
    admission_date = models.DateTimeField(
        auto_now_add=True, help_text="Date of patient admission"
    )
    name = models.CharField(max_length=50, blank=True, help_text="Patient name")
    surname = models.CharField(max_length=50, blank=True, help_text="Patient surname")
    PESEL = models.IntegerField(blank=True, null=True, help_text="Patient PESEL number")
    birth_date = models.DateField(blank=True, null=True, help_text="Patient birth date")
    sex = models.CharField(
        choices=SEX, blank=True, help_text="Patient sex", max_length=6
    )
    address = models.CharField(blank=True, help_text="Patient address", max_length=100)
    phone = models.IntegerField(blank=True, null=True, help_text="Patient phone number")
    email = models.EmailField(blank=True, null=True, help_text="Patient e-mail")
    additional_info = models.TextField(
        blank=True, help_text="Additional info about patient"
    )
    bed_number = models.CharField(
        choices=BED_CHOICE, blank=True, help_text="Bed number in hospital", max_length=6
    )
    authorized_person = models.OneToOneField(
        AuthorizedPerson,
        default="No authorized person",
        on_delete=models.SET("No authorized person"),
        blank=True,
        null=True,
        help_text="Set authorized person",
        related_name="patient",
    )
    event = models.ForeignKey(
        Event,
        default="No event assigned",
        on_delete=models.SET("No event assigned"),
        help_text="Set event",
        related_name="patient",
    )
    treatment = models.OneToOneField(
        Treatment,
        on_delete=models.SET("No treatment"),
        help_text="Add treatment",
        related_name="patient",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.id}"
