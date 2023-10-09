from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from core.settings import DEFAULT_FROM_EMAIL
from patients.models import Patient

from ..forms.email_choice_form import EmailSelectionForm
from ..models import Event


class EmailFlow:
    @staticmethod
    def get_recipient(request, pk):
        event = get_object_or_404(klass=Event, pk=pk)
        users_list = get_list_or_404(klass=User)
        form = EmailSelectionForm
        return render(
            request,
            "events/email-recipient.html",
            {"title": "Email recipient", "users_list": users_list, "event": event, "form": form},
        )


def select_email(request):
    if request.method == "POST":
        form = EmailSelectionForm(request.POST)
        if form.is_valid():
            selected_email = form.cleaned_data["email"]
            # Do something with the selected email here, e.g., save it to a model.
    else:
        form = EmailSelectionForm()

    return render(request, "your_template.html", {"form": form})


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
