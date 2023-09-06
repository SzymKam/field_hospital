import random
from json import dumps

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from treatment.constants import DRUG_DOSAGE_FORM, DRUGS, UNIT_CHOICES

from ..factories.drug_factory import DrugFactory
from ..factories.treatment_factory import TreatmentFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class TestDrugResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.drug_1 = DrugFactory()
        self.drug_2 = DrugFactory()
        self.url_list = reverse("api-drug-list")
        self.url_detail = reverse("api-drug-detail", kwargs={"pk": self.drug_1.id})
        self.headers = {"content_type": "application/json"}

    def test_list_get_not_logged_user_return_403(self) -> None:
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_list_get_logged_user_return_right_values_with_two_objects_200(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["id"], self.drug_1.id)
        self.assertEqual(response.data[0]["name"], self.drug_1.name)
        self.assertEqual(response.data[0]["dose"], self.drug_1.dose)
        self.assertEqual(response.data[0]["unit"], self.drug_1.unit)
        self.assertEqual(response.data[0]["dosage_form"], self.drug_1.dosage_form)
        self.assertEqual(response.data[0]["treatment"], self.drug_1.treatment.id)
        self.assertEqual(response.data[1]["id"], self.drug_2.id)
        self.assertEqual(response.data[1]["name"], self.drug_2.name)
        self.assertEqual(response.data[1]["dose"], self.drug_2.dose)
        self.assertEqual(response.data[1]["unit"], self.drug_2.unit)
        self.assertEqual(response.data[1]["dosage_form"], self.drug_2.dosage_form)
        self.assertEqual(response.data[1]["treatment"], self.drug_2.treatment.id)

    def test_list_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_return_201(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": random.choice(DRUGS)[0],
            "dose": fake.pyfloat(),
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["dose"], data["dose"])
        self.assertEqual(response.data["unit"], data["unit"])
        self.assertEqual(response.data["dosage_form"], data["dosage_form"])
        self.assertEqual(response.data["treatment"], data["treatment"])

    def test_list_post_logged_user_invalid_data_invalid_name_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": "its_name",
            "dose": fake.pyfloat(),
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["name"], [ErrorDetail(string='"its_name" is not a valid choice.', code="invalid_choice")]
        )

    def test_list_post_logged_user_invalid_data_invalid_dose_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": random.choice(DRUGS)[0],
            "dose": "dose",
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["dose"], [ErrorDetail(string="A valid number is required.", code="invalid")])

    def test_list_post_logged_user_invalid_data_invalid_unit_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": random.choice(DRUGS)[0],
            "dose": fake.pyfloat(),
            "unit": "unit",
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["unit"], [ErrorDetail(string='"unit" is not a valid choice.', code="invalid_choice")]
        )

    def test_list_post_logged_user_invalid_data_invalid_dosage_form_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": random.choice(DRUGS)[0],
            "dose": fake.pyfloat(),
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": "dosage",
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["dosage_form"], [ErrorDetail(string='"dosage" is not a valid choice.', code="invalid_choice")]
        )

    def test_list_post_logged_user_invalid_data_invalid_treatment_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "name": random.choice(DRUGS)[0],
            "dose": fake.pyfloat(),
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
            "treatment": "treatment",
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["treatment"],
            [ErrorDetail(string="Incorrect type. Expected pk value, received str.", code="incorrect_type")],
        )

    def test_list_patch_not_logged_user_return_403(self) -> None:
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_patch_logged_user_return_405(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_delete_not_logged_user_return_403(self) -> None:
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_list_delete_logged_user_return_405(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_get_not_logged_user_return_403(self) -> None:
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_return_right_values_200(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["id"], self.drug_1.id)
        self.assertEqual(response.data["name"], self.drug_1.name)
        self.assertEqual(response.data["dose"], self.drug_1.dose)
        self.assertEqual(response.data["unit"], self.drug_1.unit)
        self.assertEqual(response.data["dosage_form"], self.drug_1.dosage_form)
        self.assertEqual(response.data["treatment"], self.drug_1.treatment.id)

    def test_detail_get_logged_user_invalid_id_return_error_404(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_detail_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_return_405(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_patch_not_logged_user_return_403(self) -> None:
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_return_200(self) -> None:
        self.client.force_login(user=self.user)

        data = {
            "name": random.choice(DRUGS)[0],
            "dose": fake.pyfloat(),
            "unit": random.choice(UNIT_CHOICES)[0],
            "dosage_form": random.choice(DRUG_DOSAGE_FORM)[0],
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["dose"], data["dose"])
        self.assertEqual(response.data["unit"], data["unit"])
        self.assertEqual(response.data["dosage_form"], data["dosage_form"])

    def test_detail_patch_logged_user_invalid_data_return_400(self) -> None:
        self.client.force_login(user=self.user)

        data = {
            "name": "name",
            "dose": "dose",
            "unit": "unit",
            "dosage_form": "dosage_form",
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["dose"], [ErrorDetail(string="A valid number is required.", code="invalid")])
        self.assertEqual(
            response.data["name"], [ErrorDetail(string='"name" is not a valid choice.', code="invalid_choice")]
        )
        self.assertEqual(
            response.data["unit"], [ErrorDetail(string='"unit" is not a valid choice.', code="invalid_choice")]
        )
        self.assertEqual(
            response.data["dosage_form"],
            [ErrorDetail(string='"dosage_form" is not a valid choice.', code="invalid_choice")],
        )

    def test_detail_patch_logged_user_invalid_id_return_404(self) -> None:
        self.client.force_login(user=self.user)

        response = self.client.patch(path=reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["detail"], ErrorDetail(string="Not found.", code="not_found"))

    def test_detail_delete_not_logged_user_return_403(self) -> None:
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_return_204(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_invalid_id_return_404(self) -> None:
        self.client.force_login(user=self.user)
        response = self.client.delete(path=reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
