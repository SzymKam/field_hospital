from django.db import models

from ..constants import VITAL_SIGN_NAME
from .treatment_model import Treatment


class VitalSign(models.Model):
    name = models.CharField(choices=VITAL_SIGN_NAME, help_text="Choose parameter", max_length=15)
    value = models.IntegerField(help_text="Enter value")
    extra_value = models.IntegerField(help_text="DIA BP value", blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    treatment = models.ForeignKey(
        Treatment,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        help_text="Add vital sign",
        related_name="vital_sign",
    )

    def __str__(self):
        if self.extra_value:
            return f"{self.name} - {self.value}/{self.extra_value}"
        return f"{self.name} - {self.value}"
