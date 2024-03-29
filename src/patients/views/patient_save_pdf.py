from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

from patients.models import Patient
from treatment.models.drug_model import Drug
from treatment.models.treatment_model import Treatment
from treatment.models.vital_sign_model import VitalSign

from ..models import Event


class PDFPatientView(View, LoginRequiredMixin):
    def get(self, request: HttpRequest, event_pk: int, patient_pk: int):
        event = get_object_or_404(Event, pk=event_pk)
        patient = get_object_or_404(Patient, pk=patient_pk)
        treatment = get_object_or_404(klass=Treatment, pk=patient.treatment.id)
        vital_signs = VitalSign.objects.filter(treatment=treatment)
        drugs = Drug.objects.filter(treatment=treatment)

        return self._render_pdf_view(
            request=request, event=event, patient=patient, drugs=drugs, vital_signs=vital_signs
        )

    @staticmethod
    def _render_pdf_view(
        request: HttpRequest,
        event: Event,
        patient: Patient,
        drugs: QuerySet[Drug],
        vital_signs: QuerySet[VitalSign],
    ):
        template_path = "patients/patient-detail-pdf.html"

        context = {"patient": patient, "event": event, "drugs": drugs, "vital_signs": vital_signs}

        pdf_file = HttpResponse(content_type="application/pdf")
        pdf_file["Content-Disposition"] = f'attachment; filename="{patient.surname} {patient.name}-detail.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=pdf_file)

        if pisa_status.err:
            return HttpResponse("We had some errors <pre>" + html + "</pre>")

        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)

        return pdf_file
