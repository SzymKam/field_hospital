from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from core.settings import DEFAULT_FROM_EMAIL
from patients.models import Patient

from ..models import Event


@login_required()
def send_patient_list(request, pk):
    event = get_object_or_404(klass=Event, pk=pk)
    patients_list = get_list_or_404(klass=Patient, event=event)
    template_name = "events/email-template.html"
    subject = f"Patient list of {event.name}"
    context = {subject: "suka"}
    message = render_to_string(template_name, context)

    from_email = DEFAULT_FROM_EMAIL
    recipient_list = [
        "szymon15kaminski@gmail.com",
    ]

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)

    return redirect("detail-events", pk=pk)
