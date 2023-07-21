from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
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
        form = PatientForm(request.POST or None, initial={"event": initial_event.pk})
        if request.method == "POST" and form.is_valid():
            print(form["event"])
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

    def form(self):
        patient = get_object_or_404(klass=Patient, pk=self.kwargs["pk"])
        form = DetailPatientForm(instance=patient)
        return form

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Patient detail"
        context["form"] = self.form()
        return context

    # todo - add login required
