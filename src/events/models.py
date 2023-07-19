from django.db import models

from .constants import EVENT_STATUS


class Event(models.Model):
    start_date = models.DateField(auto_now=True)
    name = models.CharField(
        max_length=100, default="Event", help_text="Enter event name"
    )
    description = models.CharField(
        max_length=200, blank=True, null=True, help_text="Enter description"
    )
    localization = models.CharField(
        max_length=50, blank=True, null=True, help_text="Enter localization"
    )
    status = models.CharField(choices=EVENT_STATUS, default="Preparing", max_length=20)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
