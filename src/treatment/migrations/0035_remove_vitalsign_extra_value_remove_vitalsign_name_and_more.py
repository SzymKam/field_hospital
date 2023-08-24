# Generated by Django 4.2.3 on 2023-08-22 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0034_remove_vitalsign_additional_info"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vitalsign",
            name="extra_value",
        ),
        migrations.RemoveField(
            model_name="vitalsign",
            name="name",
        ),
        migrations.RemoveField(
            model_name="vitalsign",
            name="value",
        ),
        migrations.AddField(
            model_name="vitalsign",
            name="bp_dia",
            field=models.IntegerField(
                blank=True,
                help_text="Value of diastolic blood pressure",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0, "BP cannot be under zero"),
                    django.core.validators.MaxValueValidator(350, "Max diastolic BP is limited to 250mmHg"),
                ],
            ),
        ),
        migrations.AddField(
            model_name="vitalsign",
            name="bp_sys",
            field=models.IntegerField(
                blank=True,
                help_text="Value of systolic blood pressure",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0, "BP cannot be under zero"),
                    django.core.validators.MaxValueValidator(350, "Max systolic BP is limited to 350mmHg"),
                ],
            ),
        ),
        migrations.AddField(
            model_name="vitalsign",
            name="hr",
            field=models.IntegerField(
                blank=True,
                help_text="Heart rate value",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0, "HR cannot be under zero"),
                    django.core.validators.MaxValueValidator(350, "Max HR is limited to 350/min "),
                ],
            ),
        ),
        migrations.AddField(
            model_name="vitalsign",
            name="spo2",
            field=models.IntegerField(
                blank=True,
                help_text="Saturation value",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0, "SpO2 cannot be under 0%"),
                    django.core.validators.MaxValueValidator(100, "SpO2 cannot be over 100%"),
                ],
            ),
        ),
    ]