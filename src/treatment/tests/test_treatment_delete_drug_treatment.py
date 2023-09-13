from django.test import Client, TestCase
from django.urls import reverse_lazy
from rest_framework import status

from api.tests.factories.drug_factory import DrugFactory
from api.tests.factories.event_factory import EventFactory
from api.tests.factories.patient_factory import PatientFactory
from api.tests.factories.treatment_factory import TreatmentFactory
from api.tests.factories.user_factory import UserFactory


class DeleteDrugTreatmentTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user = UserFactory()
        self.event = EventFactory()
        self.patient = PatientFactory(event=self.event)
        self.treatment = TreatmentFactory(patient=self.patient)
        self.drug = DrugFactory(treatment=self.treatment)

        self.patient.treatment = self.treatment
        self.patient.save()

        self.url = reverse_lazy(
            "delete-drug-treatment",
            kwargs={
                "event": self.event.id,
                "patient": self.patient.id,
                "treatment": self.treatment.id,
                "pk": self.drug.id,
            },
        )

    def test_get_not_logged_user_return_302(self) -> None:
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_200(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_not_logged_user_return_302(self) -> None:
        response = self.client.post(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_302(self) -> None:
        self.client.force_login(self.user)
        response = self.client.post(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_not_logged_user_return_302(self) -> None:
        response = self.client.patch(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_return_405(self) -> None:
        self.client.force_login(self.user)
        response = self.client.patch(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_302(self) -> None:
        response = self.client.delete(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_302(self) -> None:
        self.client.force_login(self.user)
        response = self.client.delete(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
