# Generated by Django 4.2.3 on 2023-08-09 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0023_remove_treatment_drugs_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="treatment",
            name="drugs",
        ),
        migrations.AddField(
            model_name="drug",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                help_text="Add drug",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="treatment.treatment",
            ),
        ),
    ]
