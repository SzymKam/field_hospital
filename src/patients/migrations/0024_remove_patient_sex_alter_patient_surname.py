# Generated by Django 4.2.3 on 2023-07-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0023_alter_patient_name_alter_patient_surname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="sex",
        ),
        migrations.AlterField(
            model_name="patient",
            name="surname",
            field=models.CharField(
                default="NN 07-21-2023 23:42:14",
                help_text="Patient surname",
                max_length=50,
            ),
        ),
    ]
