# Generated by Django 4.2.3 on 2023-07-13 19:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatment', '0002_drug_alter_treatment_drugs'),
    ]

    operations = [
        migrations.CreateModel(
            name='VitalSign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BP', 'BP'), ('HR', 'HR'), ('RR', 'RR'), ('SpO2', 'SpO2'), ('Temperature', 'Temperature'), ('Glucose', 'Glucose'), ('GCS', 'GCS')], help_text='Choose parameter', max_length=15)),
                ('value', models.CharField(help_text='Enter value', max_length=20)),
                ('datetime', models.DateTimeField(verbose_name=datetime.datetime(2023, 7, 13, 21, 0, 4, 792173))),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='vital_sign',
            field=models.ForeignKey(blank=True, help_text='Vital signs of patient', max_length=50, on_delete=django.db.models.deletion.CASCADE, to='treatment.vitalsign'),
        ),
    ]
