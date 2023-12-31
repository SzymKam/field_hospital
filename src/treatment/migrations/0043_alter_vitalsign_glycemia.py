# Generated by Django 4.2.3 on 2023-08-30 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0042_alter_vitalsign_glycemia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vitalsign",
            name="glycemia",
            field=models.IntegerField(
                blank=True,
                help_text="Patient blood glucose level",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1, "Glycemia cannot be under 1"),
                    django.core.validators.MaxValueValidator(900, "Glycemia level is limited to 900"),
                ],
                verbose_name="Glucose level",
            ),
        ),
    ]
