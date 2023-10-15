from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, get_list_or_404, get_object_or_404
from django.template.loader import get_template
from django.views import View
from weasyprint import HTML

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

        pdf_file = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(content_type="text/pdf")
        response["Content-Disposition"] = f'attachment; filename="{event.name}-detail.pdf"'
        response.write(pdf_file)

        return response
