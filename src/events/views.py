from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from typing import Any
from .models import Event
from .forms import EventForm
from patients.models import Patient


class AllActiveEventView(ListView):
    template_name = "events/events-list.html"
    queryset = (
        Event.objects.filter(status="Preparing").values()
        | Event.objects.filter(status="In progress").values()
    )

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Active events list"
        return context

    # todo - add login required


class AllInactiveEventView(ListView):
    template_name = "events/events-list-complete.html"
    queryset = Event.objects.filter(status="Ended").values()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Inactive events list"
        return context

    # todo - add login required


class DetailEventView(DetailView):
    template_name = "events/events-detail.html"
    queryset = Event.objects.all()

    @staticmethod
    def get_all_patients_from_event(event_id: int) -> list[Patient]:
        patients = Patient.objects.filter(event=event_id)
        return patients

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["patients"] = self.get_all_patients_from_event(event_id=self.object.id)
        context["title"] = f"Event - {self.object.name}"
        return context

    # todo - add login required


class CreateEventView(CreateView):
    model = Event
    template_name = "events/events-new.html"
    form_class = EventForm
    queryset = Event.objects.all()
    success_url = reverse_lazy("all-events")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create new event"
        return context

    # todo add permissions, login_url


class UpdateEventView(UpdateView):
    model = Event
    template_name = "events/events-update.html"
    form_class = EventForm

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update event"
        return context

    def get_success_url(self):
        return reverse_lazy("detail-events", args=(self.object.id,))

    # todo add permissions, login_url, succes_url,


class DeleteEventView(DeleteView):
    model = Event
    template_name = "events/events-delete.html"
    success_url = reverse_lazy("complete-events")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete event"
        return context

    # todo add permissions, messages, login_url, succes_url, override form_valid for succes message
