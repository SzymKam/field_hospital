# Generated by Django 4.2.3 on 2023-07-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0003_event_description_event_localization_event_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(
                default="Event", help_text="Enter event name", max_length=100
            ),
        ),
    ]
