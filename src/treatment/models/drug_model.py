from django.db import models

from .treatment_model import Treatment
from treatment.constants import (
    DRUG_AND_FLUID_CHOICES,
    DRUG_DOSAGE_FORM,
    UNIT_CHOICES,
)


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
