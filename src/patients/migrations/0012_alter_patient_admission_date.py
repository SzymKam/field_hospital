# Generated by Django 4.2.3 on 2023-07-16 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0011_rename_e_mail_patient_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="admission_date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 16, 9, 45, 1, 734405),
                help_text="Date of patient admission",
            ),
        ),
    ]