# Generated by Django 4.2.3 on 2024-01-08 07:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("events", "0001_initial"),
        ("treatment", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthorizedPerson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(help_text="Person name", max_length=50)),
                ("surname", models.CharField(help_text="Person surname", max_length=50)),
                ("phone", models.IntegerField(blank=True, help_text="Person phone number", null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "admission_date",
                    models.DateTimeField(default=django.utils.timezone.now, help_text="Date of patient admission"),
                ),
                ("name", models.CharField(blank=True, help_text="Patient name", max_length=50)),
                ("surname", models.CharField(blank=True, help_text="Patient surname", max_length=50)),
                (
                    "priority",
                    models.CharField(
                        blank=True,
                        choices=[("RED", "RED"), ("YELLOW", "YELLOW"), ("GREEN", "GREEN")],
                        help_text="Priority",
                        max_length=6,
                        null=True,
                    ),
                ),
                ("PESEL", models.BigIntegerField(blank=True, help_text="Patient PESEL number", null=True)),
                ("birth_date", models.DateField(blank=True, help_text="Patient birth date", null=True)),
                ("address", models.CharField(blank=True, help_text="Patient address", max_length=100)),
                ("phone", models.BigIntegerField(blank=True, help_text="Patient phone number", null=True)),
                ("email", models.EmailField(blank=True, help_text="Patient e-mail", max_length=254, null=True)),
                ("additional_info", models.TextField(blank=True, help_text="Additional info about patient")),
                (
                    "bed_number",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("No bed", "No bed"),
                            ("ALS", "ALS"),
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                            ("11", "11"),
                            ("12", "12"),
                            ("13", "13"),
                            ("14", "14"),
                            ("15", "15"),
                            ("16", "16"),
                            ("17", "17"),
                            ("18", "18"),
                            ("19", "19"),
                            ("20", "20"),
                            ("21", "21"),
                            ("22", "22"),
                            ("23", "23"),
                            ("24", "24"),
                            ("25", "25"),
                        ],
                        default="No bed",
                        help_text="Bed number in hospital",
                        max_length=6,
                    ),
                ),
                ("status", models.CharField(default="Active", max_length=20)),
                (
                    "authorized_person",
                    models.OneToOneField(
                        blank=True,
                        help_text="Set authorized person",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="patients.authorizedperson",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        help_text="Set event",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="events.event",
                    ),
                ),
                (
                    "treatment",
                    models.OneToOneField(
                        blank=True,
                        help_text="Add treatment",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="treatment.treatment",
                    ),
                ),
            ],
        ),
    ]
