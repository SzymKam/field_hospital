from django.contrib import admin

from treatment.models.drug_model import Drug
from treatment.models.treatment_model import MedicalStaff
from treatment.models.vital_sign_model import VitalSign


@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass


@admin.register(VitalSign)
class VitalSignAdmin(admin.ModelAdmin):
    pass
