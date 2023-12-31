from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from events.models import Event
from patients.models import Patient
from treatment.forms.treatment_forms import (
    CreateTreatmentForm,
    UpdateTreatmentDescriptionForm,
    UpdateTreatmentDiagnosisForm,
    UpdateTreatmentInterviewForm,
    UpdateTreatmentMedicalStaffForm,
)
from treatment.models.drug_model import Drug
from treatment.models.treatment_model import Treatment
from treatment.models.vital_sign_model import VitalSign

from .vital_signs_plot import TreatmentPlot


def get_event_and_patient(event_id: int, patient_id: int) -> dict:
    event = get_object_or_404(klass=Event, pk=event_id)
    patient = get_object_or_404(klass=Patient, pk=patient_id)
    return {"event": event, "patient": patient}


class CreateTreatmentView(LoginRequiredMixin, CreateView):
    model = Treatment
    template_name = "treatment/treatment-new.html"
    form_class = CreateTreatmentForm
    queryset = Treatment.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add medic into treatment"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def form_valid(self, form: Any):
        treatment = form.save()
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        patient.treatment = treatment
        patient.save()
        return super().form_valid(form)

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class DetailTreatmentView(LoginRequiredMixin, DetailView):
    template_name = "treatment/treatment-detail.html"
    queryset = Treatment.objects.all()

    def get_drugs_and_vital_signs(self) -> dict[str, Any]:
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        vital_signs = VitalSign.objects.filter(treatment=treatment)
        drugs = Drug.objects.filter(treatment=treatment)
        graph = TreatmentPlot.create_plot(treatment=treatment)
        return {"drugs": drugs, "vital_signs": vital_signs, "graph": graph}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment detail"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        context.update(self.get_drugs_and_vital_signs())
        return context


class UpdateTreatmentInterviewView(LoginRequiredMixin, UpdateView):
    template_name = "treatment/treatment-edit-interview.html"
    model = Treatment
    form_class = UpdateTreatmentInterviewForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - interview"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentDescriptionView(LoginRequiredMixin, UpdateView):
    template_name = "treatment/treatment-edit-description.html"
    model = Treatment
    form_class = UpdateTreatmentDescriptionForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - interview"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentMedicalStaffView(LoginRequiredMixin, UpdateView):
    template_name = "treatment/treatment-edit-medical-staff.html"
    model = Treatment
    form_class = UpdateTreatmentMedicalStaffForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - medical staff"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentDiagnosisView(LoginRequiredMixin, UpdateView):
    template_name = "treatment/treatment-edit-diagnosis.html"
    model = Treatment
    form_class = UpdateTreatmentDiagnosisForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - diagnosis"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )
