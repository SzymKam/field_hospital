from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from patients.models import Patient

from ..models import Event


class PDFFlowView(View, LoginRequiredMixin):
    def get(self, request, event_pk):
        event = get_object_or_404(Event, pk=event_pk)
        patients_list = get_list_or_404(klass=Patient, event=event)
        return self._render_pdf_view(request=request, event=event, patients_list=patients_list)

    @staticmethod
    def _render_pdf_view(request, event: Event, patients_list: list[Patient]):
        template_path = "events/pdf-template.html"
        template = get_template(template_path)

        context = {"patients_list": patients_list, "event": event}
        html = template.render(context)

        pdf_file = HttpResponse(content_type="application/pdf")
        pdf_file["Content-Disposition"] = f'attachment; filename="{event.name}-detail.pdf"'

        pisa_status = pisa.CreatePDF(html, dest=pdf_file)

        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)

        return pdf_file
