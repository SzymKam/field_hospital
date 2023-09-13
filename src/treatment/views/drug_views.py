from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from treatment.forms.drug_form import DrugForm
from treatment.models.drug_model import Drug
from treatment.models.treatment_model import Treatment

from .treatment_views import get_event_and_patient


class CreateDrugView(LoginRequiredMixin, CreateView):
    model = Drug
    template_name = "treatment/treatment-edit-drug.html"
    form_class = DrugForm
    queryset = Drug.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new drug to patient"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def form_valid(self, form: Any):
        drug = form.save()
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        drug.treatment = treatment
        drug.save()
        return super().form_valid(form)

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.kwargs["pk"]},
        )


class UpdateDrugView(LoginRequiredMixin, UpdateView):
    model = Drug
    template_name = "treatment/treatment-edit-drug.html"
    form_class = DrugForm
    queryset = Drug.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit drug"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.kwargs["treatment"]},
        )


class DeleteDrugView(LoginRequiredMixin, DeleteView):
    model = Drug
    template_name = "treatment/treatment-delete-drug.html"

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete drug"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.kwargs["treatment"]},
        )
