# Generated by Django 4.2.3 on 2023-08-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0026_drug_dose_drug_unit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="drug",
            name="dose",
            field=models.FloatField(blank=True, help_text="Dose of drug", null=True),
        ),
    ]