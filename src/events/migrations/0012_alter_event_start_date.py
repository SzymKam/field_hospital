# Generated by Django 4.2.3 on 2023-09-02 16:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0011_alter_event_localization_alter_event_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
