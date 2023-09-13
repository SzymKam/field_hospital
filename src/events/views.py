import datetime
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from patients.models import Patient

from .forms import CloseEventForm, EventForm
from .models import Event


class CreateEventView(LoginRequiredMixin, CreateView):
    model = Event
    template_name = "events/events-new.html"
    form_class = EventForm
    queryset = Event.objects.all()
    success_url = reverse_lazy("all-events")
    extra_context = {"title": "Create new event"}


class AllActiveEventView(LoginRequiredMixin, ListView):
    template_name = "events/events-list.html"
    queryset = Event.objects.filter(status="Preparing").values() | Event.objects.filter(status="In progress").values()
    extra_context = {"title": "Active events list"}


class AllInactiveEventView(LoginRequiredMixin, ListView):
    template_name = "events/events-list-complete.html"
    queryset = Event.objects.filter(status="Ended").values()
    extra_context = {"title": "Inactive events list"}


class DetailEventView(LoginRequiredMixin, DetailView):
    template_name = "events/events-detail.html"
    queryset = Event.objects.all()

    @staticmethod
    def get_all_patients_from_event(event_id: int) -> QuerySet[Patient]:
        patients = Patient.objects.filter(event=event_id)
        return patients

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["patients"] = self.get_all_patients_from_event(event_id=self.object.id)
        context["title"] = f"Event - {self.object.name}"
        return context


class UpdateEventView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = "events/events-update.html"
    form_class = EventForm
    extra_context = {"title": "Update event"}

    def get_success_url(self):
        return reverse_lazy("detail-events", args=(self.object.id,))


class CloseRestoreEventView(LoginRequiredMixin):
    @staticmethod
    def close_event(request, pk: int) -> HttpResponse:
        event_to_close = get_object_or_404(klass=Event, pk=pk)
        form = CloseEventForm(
            request.POST or None,
            instance=event_to_close,
            initial={"end_date": datetime.date.today()},
        )
        if request.method == "POST" and form.is_valid():
            event_to_close.status = "Ended"
            event_to_close.save()
            form.save()
            return redirect("detail-events", pk=pk)
        return render(
            request,
            "events/events-close.html",
            {"title": "Closing event", "event": event_to_close, "form": form},
        )

    @staticmethod
    def restore_event(request, pk: int) -> HttpResponse:
        event_to_restore = get_object_or_404(klass=Event, pk=pk)
        event_to_restore.status = "In progress"
        event_to_restore.save()
        return redirect("detail-events", pk=pk)


class DeleteEventView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = "events/events-delete.html"
    success_url = reverse_lazy("complete-events")
    extra_context = {"title": "Delete event"}
