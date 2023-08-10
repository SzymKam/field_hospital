from django.db import models
from .treatment_model import Treatment
from ..constants import VITAL_SIGN_NAME


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

    def __str__(self):
        return f"{self.name} - {self.value}"
