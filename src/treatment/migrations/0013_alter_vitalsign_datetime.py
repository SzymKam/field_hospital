# Generated by Django 4.2.3 on 2023-07-16 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0012_alter_vitalsign_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vitalsign",
            name="datetime",
            field=models.DateTimeField(
                verbose_name=datetime.datetime(2023, 7, 16, 15, 17, 39, 831377)
            ),
        ),
    ]
