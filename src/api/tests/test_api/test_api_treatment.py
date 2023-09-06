from json import dumps

from django.test import TestCase, tag
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.medical_staff_factory import MedicalStaffFactory
from ..factories.patient_factory import PatientFactory
from ..factories.treatment_factory import TreatmentFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class TestTreatmentResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.treatment_1 = TreatmentFactory()
        self.treatment_2 = TreatmentFactory()
        self.url_list = reverse("api-treatment-list")
        self.url_detail = reverse("api-treatment-detail", kwargs={"pk": self.treatment_1.id})
        self.data = {
            "interview": fake.text(),
            "description": fake.text(),
            "diagnosis": fake.name(),
            "medical_staff": MedicalStaffFactory().id,
            "patient": PatientFactory().id,
        }
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

        self.assertEqual(response.data[0]["interview"], self.treatment_1.interview)
        self.assertEqual(response.data[0]["description"], self.treatment_1.description)
        self.assertEqual(response.data[0]["diagnosis"], self.treatment_1.diagnosis)
        self.assertEqual(response.data[0]["medical_staff"], self.treatment_1.medical_staff.id)

        self.assertEqual(response.data[1]["interview"], self.treatment_2.interview)
        self.assertEqual(response.data[1]["description"], self.treatment_2.description)
        self.assertEqual(response.data[1]["diagnosis"], self.treatment_2.diagnosis)
        self.assertEqual(response.data[1]["medical_staff"], self.treatment_2.medical_staff.id)

    def test_list_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_return_201(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "interview": fake.text(),
            "description": fake.text(),
            "diagnosis": fake.name(),
            "medical_staff": MedicalStaffFactory().id,
            "patient": PatientFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["interview"], data["interview"])
        self.assertEqual(response.data["description"], data["description"])
        self.assertEqual(response.data["diagnosis"], data["diagnosis"])
        self.assertEqual(response.data["medical_staff"], data["medical_staff"])
        self.assertEqual(response.data["patient"], data["patient"])

    def test_list_post_logged_user_invalid_data_no_patient_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "interview": fake.text(),
            "description": fake.text(),
            "diagnosis": fake.name(),
            "medical_staff": MedicalStaffFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["patient"], [ErrorDetail(string="This field is required.", code="required")])

    def test_list_post_logged_user_invalid_medical_staff_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "interview": fake.text(),
            "description": fake.text(),
            "diagnosis": fake.name(),
            "medical_staff": "medical_staff_str",
            "patient": PatientFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["medical_staff"],
            [ErrorDetail(string="Incorrect type. Expected pk value, received str.", code="incorrect_type")],
        )

    def test_list_post_logged_user_too_long_value_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "interview": fake.text(),
            "description": fake.text(),
            "diagnosis": fake.text() + fake.text(),
            "medical_staff": "medical_staff_str",
            "patient": PatientFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["diagnosis"],
            [ErrorDetail(string="Ensure this field has no more than 100 characters.", code="max_length")],
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
        self.assertEqual(response.data["id"], self.treatment_1.id)
        self.assertEqual(response.data["interview"], self.treatment_1.interview)
        self.assertEqual(response.data["description"], self.treatment_1.description)
        self.assertEqual(response.data["diagnosis"], self.treatment_1.diagnosis)

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

        data = {"medical_staff": MedicalStaffFactory().id, "patient": PatientFactory().id}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["patient"], data["patient"])
        self.assertEqual(response.data["medical_staff"], data["medical_staff"])

    def test_detail_patch_logged_user_invalid_data_return_400(self) -> None:
        self.client.force_login(user=self.user)

        data = {"medical_staff": "no_medical"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), **self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["medical_staff"],
            [ErrorDetail(string="Incorrect type. Expected pk value, received str.", code="incorrect_type")],
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
