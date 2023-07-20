from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from typing import Any
from .models import Patient
from .forms import PatientForm


class CreatePatientView(CreateView):
    model = Patient
    template_name = "patients/patients-new.html"
    form_class = PatientForm
    queryset = Patient.objects.all()
    success_url = reverse_lazy("all-events")

    # def get_event_id(self, request):
    #     self.event_id = request.resolver_match.kwargs['event']
    #     print(self.event_id)
    #     return self.event_id

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add patient"
        return context

    # @staticmethod
    # def get_success_url(request):
    #     return reverse_lazy("detail-events", kwargs={'pk': 4})
