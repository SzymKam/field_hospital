import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import QuerySet

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from patients.models import Patient
from events.models import Event

from treatment.forms import CreateTreatmentForm, UpdateTreatmentInterviewForm, UpdateDescriptionInterviewForm
from treatment.models import Treatment


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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "Treatment detail"
        context.update(self.get_data())
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


class UpdateDescriptionInterviewView(UpdateView):
    template_name = "treatment/treatment-edit-description.html"
    model = Treatment
    form_class = UpdateDescriptionInterviewForm

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
