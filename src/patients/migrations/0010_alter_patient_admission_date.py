# Generated by Django 4.2.3 on 2023-07-13 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0009_alter_patient_admission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='admission_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 13, 21, 9, 3, 561058), help_text='Date of patient admission'),
        ),
    ]
