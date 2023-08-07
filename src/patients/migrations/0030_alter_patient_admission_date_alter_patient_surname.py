# Generated by Django 4.2.3 on 2023-08-06 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0029_alter_patient_admission_date_alter_patient_surname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="admission_date",
            field=models.DateTimeField(default="08-06-2023 12:10", help_text="Date of patient admission"),
        ),
        migrations.AlterField(
            model_name="patient",
            name="surname",
            field=models.CharField(default="NN 08-06-2023 12:10:30", help_text="Patient surname", max_length=50),
        ),
    ]