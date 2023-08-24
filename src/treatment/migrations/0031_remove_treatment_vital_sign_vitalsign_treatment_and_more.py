# Generated by Django 4.2.3 on 2023-08-10 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0030_remove_drug_volume_alter_drug_unit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="treatment",
            name="vital_sign",
        ),
        migrations.AddField(
            model_name="vitalsign",
            name="treatment",
            field=models.ForeignKey(
                blank=True,
                help_text="Add vital sign",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vital_sign",
                to="treatment.treatment",
            ),
        ),
        migrations.AlterField(
            model_name="vitalsign",
            name="value",
            field=models.IntegerField(help_text="Enter value"),
        ),
    ]