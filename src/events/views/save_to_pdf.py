import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.staticfiles import finders
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.template.loader import get_template, render_to_string
from django.views import View
from xhtml2pdf import pisa

from core import settings
from core.settings import DEFAULT_FROM_EMAIL
from patients.models import Patient

from ..forms.email_choice_form import EmailSelectionForm
from ..models import Event

# def link_callback(uri, rel):
#     """
#     Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#     resources
#     """
#     result = finders.find(uri)
#     if result:
#         if not isinstance(result, (list, tuple)):
#             result = [result]
#         result = list(os.path.realpath(path) for path in result)
#         path = result[0]
#     else:
#         sUrl = settings.STATIC_URL  # Typically /static/
#         sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#         mUrl = settings.MEDIA_URL  # Typically /media/
#         mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/
#
#         if uri.startswith(mUrl):
#             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#         elif uri.startswith(sUrl):
#             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#         else:
#             return uri
#
#     # make sure that file exists
#     if not os.path.isfile(path):
#         raise RuntimeError(
#             'media URI must start with %s or %s' % (sUrl, mUrl)
#         )
#     return path


class PDFFlowView(View, LoginRequiredMixin):
    def get(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        patients_list = get_list_or_404(klass=Patient, event=event)
        return self._render_pdf_view(request=request, event=event, patients_list=patients_list)

    def _render_pdf_view(self, request, event, patients_list):
        template_path = "events/pdf-template.html"
        context = {"patients_list": patients_list, "event": event}

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = f'attachment; filename="{event.name}-detail.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(
            html,
            dest=response,
            # link_callback=link_callback
        )

        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")
        return response
