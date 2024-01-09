ALLOWED_MEDICAL_QUALIFICATIONS = ["First Aid", "Qualified first aid", "Midwife", "Nurse", "Paramedic", "Doctor"]

ALLOWED_EVENT_STATUS = ["Preparing", "In progress"]

ALLOWED_BED_CHOICE = [
    "No bed",
    "ALS",
] + [str(num) for num in range(1, 26)]

ALLOWED_PRIORITY_CHOICE = ["RED", "YELLOW", "GREEN"]
