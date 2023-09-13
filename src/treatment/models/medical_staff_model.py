from django.db import models

from treatment.constants import MEDICAL_QUALIFICATIONS


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
