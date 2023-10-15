from django.db import models

from ..constants import icd_10_choices
from .medical_staff_model import MedicalStaff


class Treatment(models.Model):
    """
    Represents a patient's treatment record.
    """

    interview = models.TextField(blank=True, help_text="Place for medical interview")
    description = models.TextField(blank=True, help_text="Place for patient description")
    diagnosis = models.CharField(choices=icd_10_choices(), blank=True, help_text="Diagnose?", max_length=100)
    medical_staff = models.ForeignKey(
        MedicalStaff,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Add medic to patient",
    )

    def __str__(self):
        return f"Treatment: {self.pk}"
