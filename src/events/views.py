from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import Event
from .forms import EventForm


class AllEventView(ListView):
    template_name = ""
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Events list"
        context["subtitle"] = self.object
        return context

    #todo - add login required


class DetailEventView(DetailView):
    template_name = ""
    queryset = Event.objects.all()

    @staticmethod
    def get_all_patients_from_event(event_id):
        patients = Patient.objects.filter(event=event_id)
        return patients

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patients"] = self.get_all_patients_from_event(event_id=self.object.id)
        context["title"] = f"Event {self.object.name}"
        context["subtitle"] = self.object
        return context

    # todo - add in Future all Patient objects into context and login required, when Patient object is ready


class CreateEventView(CreateView):
    model = Event
    template_name = ""
    form_class = EventForm
    queryset = Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create event"
        context["subtitle"] = "Creating new event"
        return context

    #todo add permissions, messages, login_url, succes_url, override form_valid for succes message


class UpdateEventView(UpdateView):
    model = Event
    template_name = ""
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update event"
        context["subtitle"] = "Updating new event"
        return context

    # todo add permissions, messages, login_url, succes_url, override form_valid for succes message


class DeleteEventView(DeleteView):
    model = Event
    template_name = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete event"
        context["subtitle"] = "Deleting new event"
        return context

    # todo add permissions, messages, login_url, succes_url, override form_valid for succes message
