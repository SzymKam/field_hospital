from django.db import models
from datetime import datetime
from .constants import (
    MEDICAL_QUALIFICATIONS,
    DRUG_AND_FLUID_CHOICES,
    DRUG_DOSAGE_FORM,
    FLUID_VOLUME,
    VITAL_SIGN_NAME,
)


class MedicalStaff(models.Model):
    name = models.CharField(blank=True, help_text="Medic name", max_length=50)
    surname = models.CharField(blank=True, help_text="Medic surname", max_length=50)
    medical_qualifications = models.CharField(
        choices=MEDICAL_QUALIFICATIONS,
        default="First aid",
        help_text="Qualifications of medic",
        max_length=20,
    )


class Drug(models.Model):
    name = models.CharField(
        choices=DRUG_AND_FLUID_CHOICES,
        blank=True,
        help_text="Add new drug",
        max_length=40,
    )
    dosage_form = models.CharField(
        choices=DRUG_DOSAGE_FORM,
        blank=True,
        help_text="Dosage form of drug",
        max_length=20,
    )
    volume = models.CharField(
        choices=FLUID_VOLUME, blank=True, help_text="Volume of fluid", max_length=20
    )


class VitalSign(models.Model):
    name = models.CharField(
        choices=VITAL_SIGN_NAME, help_text="Choose parameter", max_length=15
    )
    value = models.CharField(help_text="Enter value", max_length=20)
    datetime = models.DateTimeField(datetime.now())
    additional_info = models.TextField()


class Treatment(models.Model):
    interview = models.TextField(blank=True, help_text="Place for medical interview")
    vital_sign = models.ForeignKey(
        VitalSign,
        blank=True,
        help_text="Vital signs of patient",
        max_length=50,
        on_delete=models.CASCADE,
    )
    drugs = models.ForeignKey(
        Drug,
        blank=True,
        help_text="Medications given to the patient",
        max_length=50,
        on_delete=models.CASCADE,
    )
    description = models.TextField(
        blank=True, help_text="Place for patient description"
    )
    diagnosis = models.CharField(
        blank=True, help_text="Diagnose", max_length=50
    )  # todo maybe add icd10 library??
    additional_info = models.TextField(
        blank=True, help_text="Additional info about patient treatment"
    )
    medical_staff = models.ForeignKey(
        MedicalStaff,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Add medic to patient",
    )
