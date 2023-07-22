import datetime

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from typing import Any
from .models import Patient
from .forms import PatientForm, DetailPatientForm
from events.models import Event


# class CreatePatientView(CreateView):
#     model = Patient
#     template_name = "patients/patients-new.html"
#     form_class = PatientForm
#     queryset = Patient.objects.all()
#
#     def get_initial(self):
#         initial = super().get_initial()
#         initial['event'] = self.kwargs['event']
#         print(initial)
#         return initial
#
#     def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Add patient"
#         return context
#
#     success_url = reverse_lazy("detail-events", kwargs={'pk': get_initial()['event']})


class CreatePatientView:
    @staticmethod
    def create_patient(request, event: int):
        initial_event = get_object_or_404(klass=Event, pk=event)
        form = PatientForm(
            request.POST or None,
            initial={
                "event": initial_event.pk,
                "admission_date": datetime.datetime.now(),
            },
        )
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect("detail-events", pk=event)
        return render(
            request,
            "patients/patients-new.html",
            {"form": form, "title": "Add patient", "event": initial_event},
        )


class DetailPatientView(DetailView):
    template_name = "patients/patients-detail.html"
    queryset = Patient.objects.all()

    def get_data(self):
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["pk"])
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        return {"patient": patient, "event": event}

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Patient detail"
        context.update(self.get_data())
        return context

    # todo - add login required


class UpdatePatientView(UpdateView):
    template_name = "patients/patients-update.html"
    model = Patient
    form_class = DetailPatientForm

    def get_data(self):
        event = get_object_or_404(klass=Event, pk=self.kwargs["event"])
        return {"event": event}

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Patient update"
        context.update(self.get_data())
        return context

    def get_success_url(self):
        return reverse_lazy(
            "detail-patient",
            kwargs={"event": self.kwargs["event"], "pk": self.kwargs["pk"]},
        )


class DischargePatientView:
    @staticmethod
    def discharge_patient(request, pk: int, event: int) -> HttpResponse:
        patient_to_discharge = get_object_or_404(klass=Patient, pk=pk)
        event = get_object_or_404(klass=Event, pk=event)

        if request.method == "POST":
            patient_to_discharge.status = "Discharged"
            patient_to_discharge.save()
            return redirect("detail-events", pk=event.pk)
        return render(
            request,
            "patients/patients-discharge.html",
            {
                "title": "Discharging patient",
                "patient": patient_to_discharge,
                "event": event,
            },
        )
