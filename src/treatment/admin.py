from django.contrib import admin
from treatment.models.treatment_model import MedicalStaff
from treatment.models.drug_model import Drug


@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass
