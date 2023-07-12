from django.db import models


class Treatment(models.Model):
    interview = models.TextField(blank=True, help_text="Place for medical interview")
    description = models.TextField(blank=True, help_text="Place for patient description")


    diagnosis = models.CharField(help_text="Diagnose")

