from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .treatment_model import Treatment


class VitalSign(models.Model):
    bp_sys = models.IntegerField(
        help_text="Value of systolic blood pressure",
        blank=True,
        null=True,
        verbose_name="Systolic blood pressure",
        validators=[
            MinValueValidator(0, "BP cannot be under zero"),
            MaxValueValidator(350, "Max systolic BP is limited to 350mmHg"),
        ],
    )

    bp_dia = models.IntegerField(
        help_text="Value of diastolic blood pressure",
        blank=True,
        null=True,
        verbose_name="Diastolic blood pressure",
        validators=[
            MinValueValidator(0, "BP cannot be under zero"),
            MaxValueValidator(350, "Max diastolic BP is limited to 250mmHg"),
        ],
    )

    hr = models.IntegerField(
        help_text="Heart rate value",
        blank=True,
        null=True,
        verbose_name="Heart rate",
        validators=[
            MinValueValidator(0, "HR cannot be under zero"),
            MaxValueValidator(350, "Max HR is limited to 350/min "),
        ],
    )

    sao2 = models.IntegerField(
        help_text="Saturation value",
        blank=True,
        null=True,
        verbose_name="Saturation",
        validators=[MinValueValidator(30, "SaO2 too low"), MaxValueValidator(100, "Max SaO2 is limited to 100")],
    )

    temperature = models.FloatField(
        help_text="Patient temperature in *C",
        blank=True,
        null=True,
        verbose_name="Temperature",
        validators=[
            MinValueValidator(13, "Temperature limit is set to 13*C"),
            MaxValueValidator(45, "Temperature limit is set to 45*C"),
        ],
    )

    glycemia = models.IntegerField(
        help_text="Patient blood glucose level",
        blank=True,
        null=True,
        verbose_name="Glucose level",
        validators=[
            MinValueValidator(1, "Glycemia cannot be under 1"),
            MaxValueValidator(900, "Glycemia level is limited to 900"),
        ],
    )

    gcs = models.IntegerField(
        help_text="Patient GSC level",
        blank=True,
        null=True,
        verbose_name="Glasgow Coma Scale",
        validators=[MinValueValidator(3, "Minimum GCS level is 3"), MaxValueValidator(15, "Maximum GCS level is 15")],
    )

    datetime = models.DateTimeField(auto_now_add=True)

    treatment = models.ForeignKey(
        Treatment,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text="Add vital sign",
        related_name="vital_sign",
    )
