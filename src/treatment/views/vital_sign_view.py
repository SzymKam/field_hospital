from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from treatment.forms.vital_sign_form import VitalSignForm
from treatment.models.treatment_model import Treatment
from treatment.models.vital_sign_model import VitalSign

from .treatment_views import get_event_and_patient


class CreateVitalSignView(LoginRequiredMixin, CreateView):
    model = VitalSign
    template_name = "treatment/treatment-edit-vital-sign.html"
    form_class = VitalSignForm
    queryset = VitalSign.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Add new value of vital sign"
        context.update(get_event_and_patient(event_id=self.kwargs["event"], patient_id=self.kwargs["patient"]))
        return context

    def form_valid(self, form: Any):
        vital_sign = form.save()
        treatment = get_object_or_404(klass=Treatment, pk=self.kwargs["pk"])
        vital_sign.treatment = treatment
        vital_sign.save()
        return super().form_valid(form)

    def get_success_url(self) -> dict[str, Any]:
        return reverse_lazy(
            "detail-treatment",
            kwargs={"event": self.kwargs["event"], "patient": self.kwargs["patient"], "pk": self.kwargs["pk"]},
        )
