import datetime

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from typing import Any
from patients.models import Patient, AuthorizedPerson
from patients.forms import PatientForm, DetailPatientForm, AuthorizedPersonForm
from events.models import Event
from django.views import View


class CreateAuthPersonView(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        event = kwargs.get("event")
        patient = get_object_or_404(klass=Patient, pk=pk)
        form = AuthorizedPersonForm(request.POST or None)
        return render(
            request,
            "patients/auth-person-create.html",
            {"form": form, "title": "Add auth person", "patient": patient, "event": event},
        )

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        event = kwargs.get("event")
        patient = get_object_or_404(klass=Patient, pk=pk)
        form = AuthorizedPersonForm(request.POST or None)

        if form.is_valid():
            form.save()
            patient.authorized_person = form.instance
            patient.save()
            return redirect("detail-patient", pk=pk, event=event)
        return render(
            request,
            "patients/auth-person-create.html",
            {"form": form, "title": "Add auth person", "patient": patient, "event": event},
        )


class UpdateAuthPersonView(UpdateView):
    pass
