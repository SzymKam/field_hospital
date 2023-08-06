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

from treatment.forms import TreatmentForm, TreatmentCreateForm
from treatment.models import Treatment


class CreateTreatmentView(CreateView):
    model = Treatment
    template_name = "treatment/treatment-new.html"
    form_class = TreatmentCreateForm
    queryset = Treatment.objects.all()

    def get_data(self) -> dict:
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["patient"])
        return {"event": event, "patient": patient}

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Treatment"
        context.update(self.get_data())
        return context

    # todo add permissions, login_url
