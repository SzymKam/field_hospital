from django.db import models
from datetime import datetime

from src.events.models import Event

from .constants import SEX, BED_CHOICE


class Patient(models.Model):
    admission_date = models.DateTimeField(default=datetime.now(), help_text="Date of patient admission")
    name = models.CharField(max_length=50, blank=True, help_text="Patient name")
    surname = models.CharField(max_length=50, blank=True, help_text="Patient surname")
    PESEL = models.IntegerField(max_length=11, blank=True, null=True, help_text="Patient PESEL number")
    birth_date = models.DateField(blank=True, null=True, help_text="Patient birth date")
    sex = models.CharField(choices=SEX, blank=True, help_text="Patient sex")
    address = models.CharField(blank=True, help_text="Patient address")
    phone = models.IntegerField(blank=True, null=True, help_text="Patient phone number")
    e_mail = models.EmailField(blank=True, null=True, help_text="Patient e-mail")
    additional_info = models.TextField(blank=True, help_text="Additional info about patient")
    bed_number = models.CharField(choices=BED_CHOICE, blank=True, help_text="Bed number in hospital")
    auth_person = models.ForeignKey(AuthPerson, default="No authorized person", on_delete=models.SET("No authorized person"), blank=True, null=True, help_text="Set authorized person")
    event = models.ForeignKey(Event, default="No event assigned", on_delete=models.SET("No event assigned"), help_text="Set event")
    treatment = models.ForeignKey(Treatment, default="No treatment added", on_delete=models.SET("No treatment"), help_text="Add treatment")
