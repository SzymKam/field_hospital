from django.db import models

from .constants import (
    MEDICAL_QUALIFICATIONS,
    DRUG_AND_FLUID_CHOICES,
    DRUG_DOSAGE_FORM,
    VITAL_SIGN_NAME,
    UNIT_CHOICES,
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

    def __str__(self):
        return f"{self.name} {self.surname} - {self.medical_qualifications}"


class Treatment(models.Model):
    """
    Represents a patient's treatment record.
    """

    interview = models.TextField(blank=True, help_text="Place for medical interview")
    description = models.TextField(blank=True, help_text="Place for patient description")
    diagnosis = models.CharField(blank=True, help_text="Diagnose?", max_length=50)
    medical_staff = models.ForeignKey(
        MedicalStaff,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Add medic to patient",
    )

    def __str__(self):
        return f"Treatment: {self.pk}"


class Drug(models.Model):
    name = models.CharField(
        choices=DRUG_AND_FLUID_CHOICES,
        help_text="Add new drug",
        max_length=40,
    )
    dose = models.FloatField(help_text="Dose of drug", null=True)
    unit = models.CharField(help_text="Choose unit", choices=UNIT_CHOICES, max_length=3, default="mg")
    dosage_form = models.CharField(
        choices=DRUG_DOSAGE_FORM,
        blank=True,
        help_text="Dosage form of drug",
        max_length=20,
    )
    treatment = models.ForeignKey(
        Treatment, blank=True, null=True, on_delete=models.CASCADE, help_text="Add drug", related_name="drug"
    )

    def __str__(self):
        return f"{self.name}"


class VitalSign(models.Model):
    name = models.CharField(choices=VITAL_SIGN_NAME, help_text="Choose parameter", max_length=15)
    value = models.CharField(help_text="Enter value", max_length=20)
    datetime = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField()
    treatment = models.ForeignKey(
        Treatment,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text="Add vital sign",
        related_name="vital_sign",
    )
