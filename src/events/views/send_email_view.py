from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views import View

from core.settings import DEFAULT_FROM_EMAIL
from patients.models import Patient

from ..forms.email_choice_form import EmailSelectionForm
from ..models import Event


class EmailFlowView(View, LoginRequiredMixin):
    template_name = "events/email-recipient.html"

    def get(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        form = EmailSelectionForm()
        return render(
            request,
            self.template_name,
            {"title": "Email recipient", "event": event, "form": form},
        )

    def post(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        form = EmailSelectionForm(request.POST)

        if form.is_valid():
            selected_user_email = form.cleaned_data["email"]
            self._send_event_detail(request, event, selected_user_email)
            return redirect("detail-events", pk=event_pk)
        return render(
            request,
            self.template_name,
            {"title": "Email recipient", "event": event, "form": form},
        )

    def _send_event_detail(self, request, event, selected_user_email):
        patients_list = get_list_or_404(klass=Patient, event=event)
        template_name = "events/email-template.html"
        subject = f"Patient list of {event.name}"
        context = {"patients_list": patients_list, "event": event}
        message = render_to_string(template_name, context)

        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [
            selected_user_email.email,
        ]

        send_mail(
            subject=subject,
            message="",
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=message,
        )
