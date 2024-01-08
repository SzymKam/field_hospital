# Generated by Django 4.2.3 on 2024-01-08 07:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MedicalStaff",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(blank=True, help_text="Medic name", max_length=50)),
                ("surname", models.CharField(blank=True, help_text="Medic surname", max_length=50)),
                (
                    "medical_qualifications",
                    models.CharField(
                        choices=[
                            ("First Aid", "First Aid"),
                            ("Qualified first aid", "Qualified first aid"),
                            ("Midwife", "Midwife"),
                            ("Nurse", "Nurse"),
                            ("Paramedic", "Paramedic"),
                            ("Doctor", "Doctor"),
                        ],
                        default="First aid",
                        help_text="Qualifications of medic",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Treatment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("interview", models.TextField(blank=True, help_text="Place for medical interview")),
                ("description", models.TextField(blank=True, help_text="Place for patient description")),
                (
                    "diagnosis",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Abdominal Aortic Aneurysm I71.9", "Abdominal Aortic Aneurysm I71.9"),
                            ("Abdominal Pain R10.9", "Abdominal Pain R10.9"),
                            ("Acute Coronary Syndrome I24.9", "Acute Coronary Syndrome I24.9"),
                            ("Acute Kidney Injury N17.9", "Acute Kidney Injury N17.9"),
                            (
                                "Acute Respiratory Distress Syndrome (ARDS) J80",
                                "Acute Respiratory Distress Syndrome (ARDS) J80",
                            ),
                            ("Alcohol Intoxication F10.9", "Alcohol Intoxication F10.9"),
                            ("Allergic Reaction T78.4", "Allergic Reaction T78.4"),
                            ("Altered Mental Status R41.82", "Altered Mental Status R41.82"),
                            ("Anaphylaxis T78.2", "Anaphylaxis T78.2"),
                            ("Aortic Aneurysm (Abdominal) I71.9", "Aortic Aneurysm (Abdominal) I71.9"),
                            ("Aortic Aneurysm (Non-abdominal) I71.9", "Aortic Aneurysm (Non-abdominal) I71.9"),
                            ("Aortic Aneurysm (Thoracic) I71.9", "Aortic Aneurysm (Thoracic) I71.9"),
                            ("Aortic Aneurysm I71.9", "Aortic Aneurysm I71.9"),
                            ("Aortic Dissection I71.9", "Aortic Dissection I71.9"),
                            ("Aortic Regurgitation I06.9", "Aortic Regurgitation I06.9"),
                            ("Aortic Stenosis I35.0", "Aortic Stenosis I35.0"),
                            ("Appendicitis K35.9", "Appendicitis K35.9"),
                            (
                                "Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC) I42.7",
                                "Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC) I42.7",
                            ),
                            ("Aspiration T17", "Aspiration T17"),
                            ("Asthma Attack J45.901", "Asthma Attack J45.901"),
                            ("Asthma Exacerbation (Other) J45.901", "Asthma Exacerbation (Other) J45.901"),
                            ("Asthma Exacerbation J45.901", "Asthma Exacerbation J45.901"),
                            ("Atrial Fibrillation I48.91", "Atrial Fibrillation I48.91"),
                            ("Bronchiectasis J47", "Bronchiectasis J47"),
                            ("Bronchiolitis J21.9", "Bronchiolitis J21.9"),
                            ("Bronchitis J40", "Bronchitis J40"),
                            ("Burns T31.9", "Burns T31.9"),
                            ("COPD Exacerbation J44.1", "COPD Exacerbation J44.1"),
                            ("Cardiac Arrest I46.9", "Cardiac Arrest I46.9"),
                            ("Cardiogenic Shock R57.0", "Cardiogenic Shock R57.0"),
                            ("Cardiomyopathy (Arrhythmogenic) I42.7", "Cardiomyopathy (Arrhythmogenic) I42.7"),
                            ("Cardiomyopathy (Dilated) I42.0", "Cardiomyopathy (Dilated) I42.0"),
                            ("Cardiomyopathy (Hypertrophic) I42.2", "Cardiomyopathy (Hypertrophic) I42.2"),
                            ("Cardiomyopathy (Restrictive) I42.9", "Cardiomyopathy (Restrictive) I42.9"),
                            ("Cerebral Hemorrhage I61.9", "Cerebral Hemorrhage I61.9"),
                            ("Chest Pain R07.9", "Chest Pain R07.9"),
                            ("Choking T17", "Choking T17"),
                            (
                                "Chronic Obstructive Pulmonary Disease (COPD) Exacerbation J44.1",
                                "Chronic Obstructive Pulmonary Disease (COPD) Exacerbation J44.1",
                            ),
                            (
                                "Chronic Thromboembolic Pulmonary Hypertension (CTEPH) I27.8",
                                "Chronic Thromboembolic Pulmonary Hypertension (CTEPH) I27.8",
                            ),
                            ("Cluster Headache G44.0", "Cluster Headache G44.0"),
                            ("Cocaine Overdose T40.5", "Cocaine Overdose T40.5"),
                            ("Congestive Heart Failure (CHF) I50.9", "Congestive Heart Failure (CHF) I50.9"),
                            ("Coronary Artery Disease (CAD) I25.10", "Coronary Artery Disease (CAD) I25.10"),
                            ("Croup J05.0", "Croup J05.0"),
                            ("Cyanosis R23.0", "Cyanosis R23.0"),
                            ("Dehydration E86", "Dehydration E86"),
                            ("Diabetic Emergency E10.9", "Diabetic Emergency E10.9"),
                            ("Dilated Cardiomyopathy (DCM) I42.0", "Dilated Cardiomyopathy (DCM) I42.0"),
                            ("Drowning T75.1", "Drowning T75.1"),
                            ("Drug Overdose T40.9", "Drug Overdose T40.9"),
                            ("Dysrhythmia I49.9", "Dysrhythmia I49.9"),
                            ("Electrocution T75.4", "Electrocution T75.4"),
                            ("Embolism (Other) I74.9", "Embolism (Other) I74.9"),
                            ("Encephalitis G04.9", "Encephalitis G04.9"),
                            ("Fractures S22.9", "Fractures S22.9"),
                            ("Gastrointestinal Bleeding K92.2", "Gastrointestinal Bleeding K92.2"),
                            ("Head Injury S09.9", "Head Injury S09.9"),
                            (
                                "Heart Rhythm Disorders (Atrial Fibrillation) I48.91",
                                "Heart Rhythm Disorders (Atrial Fibrillation) I48.91",
                            ),
                            (
                                "Heart Rhythm Disorders (Atrial Flutter) I48.91",
                                "Heart Rhythm Disorders (Atrial Flutter) I48.91",
                            ),
                            (
                                "Heart Rhythm Disorders (Bradyarrhythmia) I49.9",
                                "Heart Rhythm Disorders (Bradyarrhythmia) I49.9",
                            ),
                            (
                                "Heart Rhythm Disorders (Supraventricular Tachycardia) I47.9",
                                "Heart Rhythm Disorders (Supraventricular Tachycardia) I47.9",
                            ),
                            (
                                "Heart Rhythm Disorders (Ventricular Fibrillation) I49.02",
                                "Heart Rhythm Disorders (Ventricular Fibrillation) I49.02",
                            ),
                            (
                                "Heart Rhythm Disorders (Ventricular Tachycardia) I47.2",
                                "Heart Rhythm Disorders (Ventricular Tachycardia) I47.2",
                            ),
                            (
                                "Heart Valve Disease (Valvular Heart Disease) I08.9",
                                "Heart Valve Disease (Valvular Heart Disease) I08.9",
                            ),
                            ("Heat Exhaustion T67.0", "Heat Exhaustion T67.0"),
                            ("Heat Stroke T67", "Heat Stroke T67"),
                            ("Hemoptysis R04.2", "Hemoptysis R04.2"),
                            ("Hemorrhage R58", "Hemorrhage R58"),
                            ("Hyperglycemia E10.9", "Hyperglycemia E10.9"),
                            (
                                "Hyperosmolar Hyperglycemic State (HHS) E11.1",
                                "Hyperosmolar Hyperglycemic State (HHS) E11.1",
                            ),
                            ("Hypertension (High Blood Pressure) I10", "Hypertension (High Blood Pressure) I10"),
                            ("Hypertensive Crisis I10", "Hypertensive Crisis I10"),
                            ("Hypertensive Emergency I10", "Hypertensive Emergency I10"),
                            (
                                "Hypertrophic Obstructive Cardiomyopathy (HOCM) I42.2",
                                "Hypertrophic Obstructive Cardiomyopathy (HOCM) I42.2",
                            ),
                            ("Hyperventilation R06.4", "Hyperventilation R06.4"),
                            ("Hypoglycemia E16.2", "Hypoglycemia E16.2"),
                            ("Hypoglycemic Emergency E16.2", "Hypoglycemic Emergency E16.2"),
                            ("Hypotension I95.9", "Hypotension I95.9"),
                            ("Hypothermia T68", "Hypothermia T68"),
                            ("Infective Endocarditis I33.9", "Infective Endocarditis I33.9"),
                            ("Intoxication (Other Substances) F10.9", "Intoxication (Other Substances) F10.9"),
                            ("Intracerebral Hemorrhage I61.9", "Intracerebral Hemorrhage I61.9"),
                            ("Laryngitis J04.9", "Laryngitis J04.9"),
                            ("Meningitis G03.9", "Meningitis G03.9"),
                            ("Mitral Regurgitation I34.9", "Mitral Regurgitation I34.9"),
                            ("Mitral Stenosis I05.9", "Mitral Stenosis I05.9"),
                            ("Myocardial Infarction I21.9", "Myocardial Infarction I21.9"),
                            ("Myocarditis I40.9", "Myocarditis I40.9"),
                            ("Non-infective Endocarditis I38.9", "Non-infective Endocarditis I38.9"),
                            ("Opioid Overdose T40.0", "Opioid Overdose T40.0"),
                            ("Overdose (Multiple Substances) T50.9", "Overdose (Multiple Substances) T50.9"),
                            ("Pericarditis (Acute) I30.9", "Pericarditis (Acute) I30.9"),
                            ("Pericarditis (Constrictive) I31.9", "Pericarditis (Constrictive) I31.9"),
                            ("Pericarditis (Effusive) I32.9", "Pericarditis (Effusive) I32.9"),
                            ("Pleural Effusion (Malignant) J91.0", "Pleural Effusion (Malignant) J91.0"),
                            ("Pleural Effusion J91.0", "Pleural Effusion J91.0"),
                            ("Pneumonia (Aspiration) J69.0", "Pneumonia (Aspiration) J69.0"),
                            ("Pneumonia (Bacterial) J18.9", "Pneumonia (Bacterial) J18.9"),
                            ("Pneumonia (Viral) J12.9", "Pneumonia (Viral) J12.9"),
                            ("Pneumonia J18.9", "Pneumonia J18.9"),
                            ("Pneumothorax J93.9", "Pneumothorax J93.9"),
                            ("Poisoning T51", "Poisoning T51"),
                            ("Psychiatric Crisis F99", "Psychiatric Crisis F99"),
                            ("Pulmonary Edema (Non-cardiogenic) J81", "Pulmonary Edema (Non-cardiogenic) J81"),
                            ("Pulmonary Edema J81", "Pulmonary Edema J81"),
                            ("Pulmonary Embolism (Recurrent) I26.92", "Pulmonary Embolism (Recurrent) I26.92"),
                            ("Pulmonary Embolism I26.90", "Pulmonary Embolism I26.90"),
                            ("Pulmonary Hemorrhage R04.2", "Pulmonary Hemorrhage R04.2"),
                            ("Pulmonary Hypertension (Other) I27.8", "Pulmonary Hypertension (Other) I27.8"),
                            ("Pulmonary Hypertension (Primary) I27.0", "Pulmonary Hypertension (Primary) I27.0"),
                            ("Pulmonary Hypertension (Secondary) I27.0", "Pulmonary Hypertension (Secondary) I27.0"),
                            (
                                "Pulmonary Hypertension (Unspecified) I27.9",
                                "Pulmonary Hypertension (Unspecified) I27.9",
                            ),
                            ("Pulmonary Regurgitation I37.1", "Pulmonary Regurgitation I37.1"),
                            ("Pulmonary Stenosis I37.0", "Pulmonary Stenosis I37.0"),
                            ("Respiratory Distress R06.0", "Respiratory Distress R06.0"),
                            ("Respiratory Failure J96.9", "Respiratory Failure J96.9"),
                            ("Rib Fracture (Multiple) S22.9", "Rib Fracture (Multiple) S22.9"),
                            ("Seizure (Generalized) G40.9", "Seizure (Generalized) G40.9"),
                            ("Seizure (Partial) G40.9", "Seizure (Partial) G40.9"),
                            ("Seizures R56.9", "Seizures R56.9"),
                            ("Sepsis A41.9", "Sepsis A41.9"),
                            ("Severe Bleeding R58", "Severe Bleeding R58"),
                            ("Shock R57.9", "Shock R57.9"),
                            ("Shortness of Breath R06.02", "Shortness of Breath R06.02"),
                            ("Status Epilepticus G41.9", "Status Epilepticus G41.9"),
                            ("Stroke (Hemorrhagic) I61.9", "Stroke (Hemorrhagic) I61.9"),
                            ("Stroke (Ischemic) I63.9", "Stroke (Ischemic) I63.9"),
                            ("Stroke I63.9", "Stroke I63.9"),
                            ("Sudden Cardiac Death I46.9", "Sudden Cardiac Death I46.9"),
                            ("Suicidal Ideation R45.851", "Suicidal Ideation R45.851"),
                            ("Syncope R55", "Syncope R55"),
                            ("Torn Aorta I71.9", "Torn Aorta I71.9"),
                            ("Traumatic Brain Injury S06.9", "Traumatic Brain Injury S06.9"),
                            ("Tricuspid Regurgitation I06.9", "Tricuspid Regurgitation I06.9"),
                            ("Tricuspid Stenosis I07.0", "Tricuspid Stenosis I07.0"),
                            ("Trigeminal Neuralgia G50.0", "Trigeminal Neuralgia G50.0"),
                            ("Tuberculosis A15.9", "Tuberculosis A15.9"),
                        ],
                        help_text="Diagnose?",
                        max_length=100,
                    ),
                ),
                (
                    "medical_staff",
                    models.ForeignKey(
                        blank=True,
                        help_text="Add medic to patient",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="treatment.medicalstaff",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VitalSign",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "bp_sys",
                    models.IntegerField(
                        blank=True,
                        help_text="Value of systolic blood pressure",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0, "BP cannot be under zero"),
                            django.core.validators.MaxValueValidator(350, "Max systolic BP is limited to 350mmHg"),
                        ],
                        verbose_name="Systolic blood pressure",
                    ),
                ),
                (
                    "bp_dia",
                    models.IntegerField(
                        blank=True,
                        help_text="Value of diastolic blood pressure",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0, "BP cannot be under zero"),
                            django.core.validators.MaxValueValidator(350, "Max diastolic BP is limited to 250mmHg"),
                        ],
                        verbose_name="Diastolic blood pressure",
                    ),
                ),
                (
                    "hr",
                    models.IntegerField(
                        blank=True,
                        help_text="Heart rate value",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0, "HR cannot be under zero"),
                            django.core.validators.MaxValueValidator(350, "Max HR is limited to 350/min "),
                        ],
                        verbose_name="Heart rate",
                    ),
                ),
                (
                    "sao2",
                    models.IntegerField(
                        blank=True,
                        help_text="Saturation value",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(30, "SaO2 too low"),
                            django.core.validators.MaxValueValidator(100, "Max SaO2 is limited to 100"),
                        ],
                        verbose_name="Saturation",
                    ),
                ),
                (
                    "temperature",
                    models.FloatField(
                        blank=True,
                        help_text="Patient temperature in *C",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(13, "Temperature limit is set to 13*C"),
                            django.core.validators.MaxValueValidator(45, "Temperature limit is set to 45*C"),
                        ],
                        verbose_name="Temperature",
                    ),
                ),
                (
                    "glycemia",
                    models.IntegerField(
                        blank=True,
                        help_text="Patient blood glucose level",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1, "Glycemia cannot be under 1"),
                            django.core.validators.MaxValueValidator(900, "Glycemia level is limited to 900"),
                        ],
                        verbose_name="Glucose level",
                    ),
                ),
                (
                    "gcs",
                    models.IntegerField(
                        blank=True,
                        help_text="Patient GSC level",
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(3, "Minimum GCS level is 3"),
                            django.core.validators.MaxValueValidator(15, "Maximum GCS level is 15"),
                        ],
                        verbose_name="Glasgow Coma Scale",
                    ),
                ),
                ("datetime", models.DateTimeField(auto_now_add=True)),
                (
                    "treatment",
                    models.ForeignKey(
                        blank=True,
                        help_text="Add vital sign",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vital_sign",
                        to="treatment.treatment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Drug",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "name",
                    models.CharField(
                        choices=[
                            (
                                "Drugs",
                                [
                                    ("ASA", "ASA"),
                                    ("Adenosine", "Adenosine"),
                                    ("Adrenalin", "Adrenalin"),
                                    ("Amiodarone", "Amiodarone"),
                                    ("Aspargin", "Aspargin"),
                                    ("Atropine", "Atropine"),
                                    ("Betaloc", "Betaloc"),
                                    ("Bicarbonate", "Bicarbonate"),
                                    ("Budesonide", "Budesonide"),
                                    ("Buscolysin", "Buscolysin"),
                                    ("Calcium", "Calcium"),
                                    ("Captopril", "Captopril"),
                                    ("Clemastine", "Clemastine"),
                                    ("Clonazepam", "Clonazepam"),
                                    ("Clopidogrel", "Clopidogrel"),
                                    ("Dexaven", "Dexaven"),
                                    ("Exacyl", "Exacyl"),
                                    ("Fentanyl", "Fentanyl"),
                                    ("Flumazenil", "Flumazenil"),
                                    ("Furosemide", "Furosemide"),
                                    ("Glucagon", "Glucagon"),
                                    ("Glucose 20% i.v.", "Glucose 20% i.v."),
                                    ("Glucose 40%", "Glucose 40%"),
                                    ("Heparin", "Heparin"),
                                    ("Hydrocortisone", "Hydrocortisone"),
                                    ("Hydroxyzine", "Hydroxyzine"),
                                    ("Ibuprofen", "Ibuprofen"),
                                    ("Ketamine", "Ketamine"),
                                    ("Ketonal", "Ketonal"),
                                    ("Lidocaine", "Lidocaine"),
                                    ("Magnesium", "Magnesium"),
                                    ("Mannitol", "Mannitol"),
                                    ("Metoclopramide", "Metoclopramide"),
                                    ("Midanium", "Midanium"),
                                    ("Morphine", "Morphine"),
                                    ("Naloxone", "Naloxone"),
                                    ("Nitrendipine", "Nitrendipine"),
                                    ("Nitromind", "Nitromid"),
                                    ("No-Spa", "No-Spa"),
                                    ("Ondansetron", "Ondansetron"),
                                    ("Pantoprazol", "Pantoprazol"),
                                    ("Paracetamol", "Paracetamol"),
                                    ("Polstigmine", "Polstigmine"),
                                    ("Propofol", "Propofol"),
                                    ("Pyralgin", "Pyralgin"),
                                    ("Relanium", "Relanium"),
                                    ("Relsed", "Relsed"),
                                    ("Rocuronium", "Rocuronium"),
                                    ("Salbutamol", "Salbutamol"),
                                    ("Suxamethonium", "Suxamethonium"),
                                    ("Ticagrelor", "Ticagrelor"),
                                    ("Torecan", "Torecan"),
                                    ("Urapidil", "Urapidil"),
                                ],
                            ),
                            (
                                "Fluids",
                                [
                                    ("Aqua", "Aqua"),
                                    ("Glucose 20%", "Glucose 20%"),
                                    ("Glucose 5%", "Glucose 5%"),
                                    ("NaCl 0.9%", "NaCl 0.9%"),
                                    ("Optilyte", "Optilyte"),
                                    ("Other", "Other"),
                                    ("Plasmalyte", "Plasmalyte"),
                                    ("Ringer", "Ringer"),
                                ],
                            ),
                        ],
                        help_text="Add new drug",
                        max_length=40,
                    ),
                ),
                ("dose", models.FloatField(help_text="Dose of drug", null=True)),
                (
                    "unit",
                    models.CharField(
                        choices=[("g", "g"), ("mg", "mg"), ("mcg", "mcg"), ("ml", "ml")],
                        default="mg",
                        help_text="Choose unit",
                        max_length=3,
                    ),
                ),
                (
                    "dosage_form",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pills", "Pills"),
                            ("Nebulizer", "Nebulizer"),
                            ("Injection", "Injection"),
                            ("Ointment / Gel", "Ointment / Gel"),
                            ("Areosol", "Areosol"),
                            ("Rectal enema", "Rectal enema"),
                        ],
                        help_text="Dosage form of drug",
                        max_length=20,
                    ),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        blank=True,
                        help_text="Add drug",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="drug",
                        to="treatment.treatment",
                    ),
                ),
            ],
        ),
    ]
