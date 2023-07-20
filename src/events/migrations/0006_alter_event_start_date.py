# Generated by Django 4.2.3 on 2023-07-20 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0005_alter_event_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]