# Generated by Django 4.2.3 on 2023-07-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0013_alter_vitalsign_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vitalsign",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
