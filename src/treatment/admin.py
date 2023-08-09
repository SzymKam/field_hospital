from django.contrib import admin
from .models import MedicalStaff, Drug


@admin.register(MedicalStaff)
class MedicalStaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    pass
