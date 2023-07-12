from django.db import models
from datetime import date

from .constants import EVENT_STATUS


class Event(models.Model):
    start_date = models.DateField(default=date.today()),
    name = models.CharField(max_length=100),
    description = models.CharField(max_length=200, blank=True, null=True),
    localization = models.CharField(max_length=50, blank=True, null=True),
    status = models.CharField(choices=EVENT_STATUS, default="In progress"),
    end_date = models.DateField(blank=True, null=True),
