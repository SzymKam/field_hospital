# Generated by Django 4.2.3 on 2023-10-12 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("treatment", "0044_alter_treatment_diagnosis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="treatment",
            name="diagnosis",
            field=models.CharField(
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
                    ("Hyperosmolar Hyperglycemic State (HHS) E11.1", "Hyperosmolar Hyperglycemic State (HHS) E11.1"),
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
                    ("Pulmonary Hypertension (Unspecified) I27.9", "Pulmonary Hypertension (Unspecified) I27.9"),
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
    ]
