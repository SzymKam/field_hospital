MEDICAL_QUALIFICATIONS = [
    ("First Aid", "First Aid"),
    ("Qualified first aid", "Qualified first aid"),
    ("Midwife", "Midwife"),
    ("Nurse", "Nurse"),
    ("Paramedic", "Paramedic"),
    ("Doctor", "Doctor"),
]

DRUGS = sorted(
    [
        ("Adrenalin", "Adrenalin"),
        ("ASA", "ASA"),
        ("Ketonal", "Ketonal"),
        ("Ibuprofen", "Ibuprofen"),
        ("Pyralgin", "Pyralgin"),
        ("Paracetamol", "Paracetamol"),
        ("Morphine", "Morphine"),
        ("Fentanyl", "Fentanyl"),
        ("Naloxone", "Naloxone"),
        ("Budesonide", "Budesonide"),
        ("Hydrocortisone", "Hydrocortisone"),
        ("Dexaven", "Dexaven"),
        ("Relanium", "Relanium"),
        ("Relsed", "Relsed"),
        ("Clonazepam", "Clonazepam"),
        ("Midanium", "Midanium"),
        ("Flumazenil", "Flumazenil"),
        ("Atropine", "Atropine"),
        ("Adenosine", "Adenosine"),
        ("Amiodarone", "Amiodarone"),
        ("Lidocaine", "Lidocaine"),
        ("Salbutamol", "Salbutamol"),
        ("Urapidil", "Urapidil"),
        ("Betaloc", "Betaloc"),
        ("No-Spa", "No-Spa"),
        ("Nitromind", "Nitromid"),
        ("Clopidogrel", "Clopidogrel"),
        ("Ticagrelor", "Ticagrelor"),
        ("Heparin", "Heparin"),
        ("Torecan", "Torecan"),
        ("Metoclopramide", "Metoclopramide"),
        ("Furosemide", "Furosemide"),
        ("Mannitol", "Mannitol"),
        ("Hydroxyzine", "Hydroxyzine"),
        ("Magnesium", "Magnesium"),
        ("Clemastine", "Clemastine"),
        ("Bicarbonate", "Bicarbonate"),
        ("Captopril", "Captopril"),
        ("Glucagon", "Glucagon"),
        ("Glucose 20% i.v.", "Glucose 20% i.v."),
        ("Glucose 40%", "Glucose 40%"),
        ("Exacyl", "Exacyl"),
        ("Ketamine", "Ketamine"),
        ("Polstigmine", "Polstigmine"),
        ("Ondansetron", "Ondansetron"),
        ("Buscolysin", "Buscolysin"),
        ("Suxamethonium", "Suxamethonium"),
        ("Calcium", "Calcium"),
        ("Propofol", "Propofol"),
        ("Pantoprazol", "Pantoprazol"),
        ("Nitrendipine", "Nitrendipine"),
        ("Rocuronium", "Rocuronium"),
        ("Aspargin", "Aspargin"),
    ]
)

FLUIDS = sorted(
    [
        ("Other", "Other"),
        ("Glucose 20%", "Glucose 20%"),
        ("Glucose 5%", "Glucose 5%"),
        ("NaCl 0.9%", "NaCl 0.9%"),
        ("Optilyte", "Optilyte"),
        ("Ringer", "Ringer"),
        ("Plasmalyte", "Plasmalyte"),
        ("Aqua", "Aqua"),
    ]
)

DRUG_AND_FLUID_CHOICES = [("Drugs", DRUGS), ("Fluids", FLUIDS)]

DRUG_DOSAGE_FORM = [
    ("Pills", "Pills"),
    ("Nebulizer", "Nebulizer"),
    ("Injection", "Injection"),
    ("Ointment / Gel", "Ointment / Gel"),
    ("Areosol", "Areosol"),
    ("Rectal enema", "Rectal enema"),
]

UNIT_CHOICES = [("g", "g"), ("mg", "mg"), ("mcg", "mcg"), ("ml", "ml")]
