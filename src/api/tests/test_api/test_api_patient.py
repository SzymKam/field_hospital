from json import dumps

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.event_factory import EventFactory
from ..factories.patient_factory import PatientFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class TestPatientResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.patient_1 = PatientFactory()
        self.patient_2 = PatientFactory()
        self.url_list = reverse("api-patient-list")
        self.url_detail = reverse("api-patient-detail", kwargs={"pk": self.patient_1.id})
        self.headers = {"content_type": "application/json"}

    def test_list_get_not_logged_user_return_403(self):
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_list_get_logged_user_return_right_values_with_two_objects_200(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["name"], self.patient_1.name)
        self.assertEqual(response.data[0]["PESEL"], int(self.patient_1.PESEL))
        self.assertEqual(response.data[0]["id"], self.patient_1.id)
        self.assertEqual(response.data[0]["phone"], int(self.patient_1.phone))
        self.assertEqual(response.data[0]["email"], self.patient_1.email)
        self.assertEqual(response.data[0]["event"], self.patient_1.event.id)

        self.assertEqual(response.data[1]["name"], self.patient_2.name)
        self.assertEqual(response.data[1]["PESEL"], int(self.patient_2.PESEL))
        self.assertEqual(response.data[1]["id"], self.patient_2.id)
        self.assertEqual(response.data[1]["phone"], int(self.patient_2.phone))
        self.assertEqual(response.data[1]["email"], self.patient_2.email)
        self.assertEqual(response.data[1]["event"], self.patient_2.event.id)

    def test_list_post_not_logged_user_return_403(self):
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_return_201(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "PESEL": fake.numerify(text="###########"),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["surname"], data["surname"])
        self.assertEqual(response.data["PESEL"], int(data["PESEL"]))
        self.assertEqual(response.data["address"], data["address"])
        self.assertEqual(response.data["phone"], int(data["phone"]))
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["additional_info"], data["additional_info"])
        self.assertEqual(response.data["event"], data["event"])

    def test_list_post_logged_user_invalid_data_invalid_event_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "PESEL": fake.numerify(text="###########"),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": "some_event",
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["event"],
            [ErrorDetail(string="Incorrect type. Expected pk value, received str.", code="incorrect_type")],
        )

    def test_list_post_logged_user_invalid_data_invalid_phone_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "PESEL": fake.numerify(text="###########"),
            "address": fake.address(),
            "phone": "some_phone",
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["phone"], [ErrorDetail(string="A valid integer is required.", code="invalid")])

    def test_list_post_logged_user_invalid_data_invalid_bed_number_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "PESEL": fake.numerify(text="###########"),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
            "bed_number": "some_number",
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["bed_number"],
            [ErrorDetail(string='"some_number" is not a valid choice.', code="invalid_choice")],
        )

    def test_list_post_logged_user_invalid_data_invalid_pesel_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.last_name(),
            "PESEL": "some_pesel",
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["PESEL"], [ErrorDetail(string="A valid integer is required.", code="invalid")])

    def test_list_post_logged_user_invalid_data_too_long_name_value_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.text(),
            "surname": fake.last_name(),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["name"],
            [ErrorDetail(string="Ensure this field has no more than 50 characters.", code="max_length")],
        )

    def test_list_post_logged_user_invalid_data_too_long_surname_value_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.text(),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": fake.email(),
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["surname"],
            [ErrorDetail(string="Ensure this field has no more than 50 characters.", code="max_length")],
        )

    def test_list_post_logged_user_invalid_data_invalid_email_return_400(self):
        self.client.force_login(user=self.user)
        data = {
            "name": fake.first_name(),
            "surname": fake.text(),
            "address": fake.address(),
            "phone": fake.numerify(text="#########"),
            "email": "its_email",
            "additional_info": fake.text(),
            "event": EventFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["email"], [ErrorDetail(string="Enter a valid email address.", code="invalid")])

    def test_list_patch_not_logged_user_return_403(self):
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_patch_logged_user_return_405(self):
        self.client.force_login(user=self.user)
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_delete_not_logged_user_return_403(self):
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_list_delete_logged_user_return_405(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_get_not_logged_user_return_403(self):
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_return_right_values_200(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["id"], self.patient_1.id)
        self.assertEqual(response.data["name"], self.patient_1.name)
        self.assertEqual(response.data["surname"], self.patient_1.surname)
        self.assertEqual(response.data["PESEL"], int(self.patient_1.PESEL))
        self.assertEqual(response.data["address"], self.patient_1.address)
        self.assertEqual(response.data["email"], self.patient_1.email)
        self.assertEqual(response.data["event"], self.patient_1.event.id)
        self.assertEqual(response.data["phone"], int(self.patient_1.phone))

    def test_detail_get_logged_user_invalid_id_return_error_404(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_detail_post_not_logged_user_return_403(self):
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_return_405(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_patch_not_logged_user_return_403(self):
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_return_200(self):
        self.client.force_login(user=self.user)

        data = {
            "name": "updated_name",
            "surname": "updated_surname",
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["surname"], data["surname"])

    def test_detail_patch_logged_user_invalid_data_return_400(self):
        self.client.force_login(user=self.user)

        data = {
            "email": "its_email",
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["email"], [ErrorDetail(string="Enter a valid email address.", code="invalid")])

    def test_detail_patch_logged_user_invalid_id_return_404(self):
        self.client.force_login(user=self.user)

        response = self.client.patch(path=reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["detail"], ErrorDetail(string="Not found.", code="not_found"))

    def test_detail_delete_not_logged_user_return_403(self):
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_return_204(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_invalid_id_return_404(self):
        self.client.force_login(user=self.user)
        response = self.client.delete(path=reverse("api-event-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
