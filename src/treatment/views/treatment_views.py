from typing import Any

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from patients.models import Patient
from events.models import Event

from treatment.forms.treatment_forms import (
    CreateTreatmentForm,
    UpdateTreatmentInterviewForm,
    UpdateTreatmentDescriptionForm,
    UpdateTreatmentMedicalStaffForm,
    UpdateTreatmentDiagnosisForm,
)
from treatment.models.treatment_model import Treatment
from treatment.models.drug_model import Drug
from treatment.forms.drug_form import DrugForm


class CreateTreatmentView(CreateView):
    model = Treatment
    template_name = "treatment/treatment-new.html"
    form_class = CreateTreatmentForm
    queryset = Treatment.objects.all()

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add medic into treatment"
        context.update(self.get_data())
        return context

    def form_valid(self, form):
        treatment = form.save()
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        patient.treatment = treatment
        patient.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )

    # todo add permissions, login_url


class DetailTreatmentView(DetailView):
    template_name = "treatment/treatment-detail.html"
    queryset = Treatment.objects.all()

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])

        return {"event": event, "patient": patient}

    def get_drugs(self):
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        drugs = Drug.objects.filter(treatment=treatment)
        return {"drugs": drugs}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment detail"
        context.update(self.get_data())
        context.update(self.get_drugs())
        return context

    # todo add permissions, login_url


class UpdateTreatmentInterviewView(UpdateView):
    template_name = "treatment/treatment-edit-interview.html"
    model = Treatment
    form_class = UpdateTreatmentInterviewForm

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - interview"
        context.update(self.get_data())
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentDescriptionView(UpdateView):
    template_name = "treatment/treatment-edit-description.html"
    model = Treatment
    form_class = UpdateTreatmentDescriptionForm

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - interview"
        context.update(self.get_data())
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentMedicalStaffView(UpdateView):
    template_name = "treatment/treatment-edit-medical-staff.html"
    model = Treatment
    form_class = UpdateTreatmentMedicalStaffForm

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - medical staff"
        context.update(self.get_data())
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class UpdateTreatmentDiagnosisView(UpdateView):
    template_name = "treatment/treatment-edit-diagnosis.html"
    model = Treatment
    form_class = UpdateTreatmentDiagnosisForm

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment - diagnosis"
        context.update(self.get_data())
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.object.id},
        )


class CreateDrugView(CreateView):
    model = Drug
    template_name = "treatment/treatment-edit-drug.html"
    form_class = DrugForm
    queryset = Drug.objects.all()

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_drug_list(self):
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        drugs = Drug.objects.filter(treatment=treatment)
        return {"drugs": drugs}

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new drug to patient"
        context.update(self.get_data())
        context.update(self.get_drug_list())
        return context

    def form_valid(self, form):
        drug = form.save()
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        drug.treatment = treatment
        drug.save()
        return super().form_valid(form)

    def get_success_url(self):
        drugs = self.get_drug_list()
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.kwargs["pk"]},
        )
