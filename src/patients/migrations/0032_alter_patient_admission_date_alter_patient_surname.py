# Generated by Django 4.2.3 on 2023-08-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0031_alter_patient_admission_date_alter_patient_surname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="admission_date",
            field=models.DateTimeField(default="08-06-2023 21:41", help_text="Date of patient admission"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="surname",
            field=models.CharField(default="NN 08-06-2023 21:41:59", help_text="Patient surname", max_length=50),
        ),
    ]
