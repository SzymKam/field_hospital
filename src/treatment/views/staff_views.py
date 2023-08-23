from typing import Any

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from ..forms.medical_staff_form import MedicalStaffForm
from ..models.medical_staff_model import MedicalStaff


class CreateMedicalStaffView(CreateView):
    model = MedicalStaff
    template_name = "treatment/treatment-medical-staff.html"
    form_class = MedicalStaffForm
    queryset = MedicalStaff.objects.all()
    success_url = reverse_lazy("staff")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Staff"
        return context

    # todo add permissions, login_url


class ListMedicalStaffView(ListView):
    template_name = "treatment/treatment-medical-staff-list.html"
    queryset = MedicalStaff.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Medical Staff List"
        return context

    # todo - add login required


class UpdateMedicalStaffView(UpdateView):
    model = MedicalStaff
    template_name = "treatment/treatment-medical-staff.html"
    form_class = MedicalStaffForm
    success_url = reverse_lazy("staff")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Staff"
        return context

    # todo add permissions, login_url


class DeleteMedialStaffView(DeleteView):
    model = MedicalStaff
    template_name = "treatment/treatment-medical-staff-delete.html"
    success_url = reverse_lazy("staff")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete staff"
        return context

    # todo add permissions, login_url
