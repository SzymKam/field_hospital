# Generated by Django 4.2.3 on 2023-07-21 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0022_alter_patient_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="name",
            field=models.CharField(blank=True, help_text="Patient name", max_length=50),
        ),
        migrations.AlterField(
            model_name="patient",
            name="surname",
            field=models.CharField(
                default="NN 07-21-2023 17:31:04",
                help_text="Patient surname",
                max_length=50,
            ),
        ),
    ]