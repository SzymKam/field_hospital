import random
from json import dumps

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.treatment_factory import TreatmentFactory
from ..factories.user_factory import UserFactory
from ..factories.vital_sign_factory import VitalSignFactory

fake = Faker()


class TestVitalSignResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.vital_sign_1 = VitalSignFactory()
        self.vital_sign_2 = VitalSignFactory()
        self.url_list = reverse("api-vital-sign-list")
        self.url_detail = reverse("api-vital-sign-detail", kwargs={"pk": self.vital_sign_1.id})
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

        self.assertEqual(response.data[0]["id"], self.vital_sign_1.id)
        self.assertEqual(response.data[0]["bp_sys"], self.vital_sign_1.bp_sys)
        self.assertEqual(response.data[0]["bp_dia"], self.vital_sign_1.bp_dia)
        self.assertEqual(response.data[0]["hr"], self.vital_sign_1.hr)
        self.assertEqual(response.data[0]["sao2"], self.vital_sign_1.sao2)
        self.assertEqual(response.data[0]["temperature"], self.vital_sign_1.temperature)
        self.assertEqual(response.data[0]["glycemia"], self.vital_sign_1.glycemia)
        self.assertEqual(response.data[0]["gcs"], self.vital_sign_1.gcs)
        self.assertEqual(response.data[0]["treatment"], self.vital_sign_1.treatment.id)

        self.assertEqual(response.data[1]["id"], self.vital_sign_2.id)
        self.assertEqual(response.data[1]["bp_sys"], self.vital_sign_2.bp_sys)
        self.assertEqual(response.data[1]["bp_dia"], self.vital_sign_2.bp_dia)
        self.assertEqual(response.data[1]["hr"], self.vital_sign_2.hr)
        self.assertEqual(response.data[1]["sao2"], self.vital_sign_2.sao2)
        self.assertEqual(response.data[1]["temperature"], self.vital_sign_2.temperature)
        self.assertEqual(response.data[1]["glycemia"], self.vital_sign_2.glycemia)
        self.assertEqual(response.data[1]["gcs"], self.vital_sign_2.gcs)
        self.assertEqual(response.data[1]["treatment"], self.vital_sign_2.treatment.id)

    def test_list_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_return_201(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "bp_sys": random.randint(1, 350),
            "bp_dia": random.randint(1, 350),
            "hr": random.randint(1, 350),
            "sao2": random.randint(30, 100),
            "temperature": random.uniform(13.0, 45.0),
            "glycemia": random.randint(1, 900),
            "gcs": random.randint(3, 15),
            "treatment": TreatmentFactory().id,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

        self.assertEqual(response.data["bp_sys"], data["bp_sys"])
        self.assertEqual(response.data["bp_dia"], data["bp_dia"])
        self.assertEqual(response.data["hr"], data["hr"])
        self.assertEqual(response.data["sao2"], data["sao2"])
        self.assertEqual(response.data["temperature"], data["temperature"])
        self.assertEqual(response.data["glycemia"], data["glycemia"])
        self.assertEqual(response.data["gcs"], data["gcs"])
        self.assertEqual(response.data["treatment"], data["treatment"])

    def test_list_post_logged_user_invalid_data_invalid_name_return_400(self) -> None:
        self.client.force_login(user=self.user)
        data = {
            "bp_sys": "systolic",
            "bp_dia": 999,
            "hr": "530",
            "sao2": 15,
            "temperature": 50.0,
            "glycemia": "glycemia_value",
            "gcs": 18,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["bp_sys"], [ErrorDetail(string="A valid integer is required.", code="invalid")])
        self.assertEqual(
            response.data["bp_dia"],
            [ErrorDetail(string="Ensure this value is less than or equal to 350.", code="max_value")],
        )
        self.assertEqual(
            response.data["hr"],
            [ErrorDetail(string="Ensure this value is less than or equal to 350.", code="max_value")],
        )
        self.assertEqual(
            response.data["sao2"],
            [ErrorDetail(string="Ensure this value is greater than or equal to 30.", code="min_value")],
        )
        self.assertEqual(
            response.data["temperature"],
            [ErrorDetail(string="Ensure this value is less than or equal to 45.", code="max_value")],
        )
        self.assertEqual(
            response.data["glycemia"], [ErrorDetail(string="A valid integer is required.", code="invalid")]
        )
        self.assertEqual(
            response.data["gcs"],
            [ErrorDetail(string="Ensure this value is less than or equal to 15.", code="max_value")],
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

        self.assertEqual(response.data["id"], self.vital_sign_1.id)
        self.assertEqual(response.data["bp_sys"], self.vital_sign_1.bp_sys)
        self.assertEqual(response.data["bp_dia"], self.vital_sign_1.bp_dia)
        self.assertEqual(response.data["hr"], self.vital_sign_1.hr)
        self.assertEqual(response.data["sao2"], self.vital_sign_1.sao2)
        self.assertEqual(response.data["temperature"], self.vital_sign_1.temperature)
        self.assertEqual(response.data["glycemia"], self.vital_sign_1.glycemia)
        self.assertEqual(response.data["gcs"], self.vital_sign_1.gcs)
        self.assertEqual(response.data["treatment"], self.vital_sign_1.treatment.id)

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
            "bp_sys": random.randint(1, 350),
            "bp_dia": random.randint(1, 350),
            "hr": random.randint(1, 350),
            "sao2": random.randint(30, 100),
            "temperature": random.uniform(13.0, 45.0),
            "glycemia": random.randint(1, 900),
            "gcs": random.randint(3, 15),
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["bp_sys"], data["bp_sys"])
        self.assertEqual(response.data["bp_dia"], data["bp_dia"])
        self.assertEqual(response.data["hr"], data["hr"])
        self.assertEqual(response.data["sao2"], data["sao2"])
        self.assertEqual(response.data["temperature"], data["temperature"])
        self.assertEqual(response.data["glycemia"], data["glycemia"])
        self.assertEqual(response.data["gcs"], data["gcs"])

    def test_detail_patch_logged_user_invalid_data_return_400(self) -> None:
        self.client.force_login(user=self.user)

        data = {
            "bp_sys": "systolic",
            "bp_dia": 889,
            "hr": "850",
            "sao2": 7,
            "temperature": 58.0,
            "glycemia": "glycemia_value",
            "gcs": 19,
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["bp_sys"], [ErrorDetail(string="A valid integer is required.", code="invalid")])
        self.assertEqual(
            response.data["bp_dia"],
            [ErrorDetail(string="Ensure this value is less than or equal to 350.", code="max_value")],
        )
        self.assertEqual(
            response.data["hr"],
            [ErrorDetail(string="Ensure this value is less than or equal to 350.", code="max_value")],
        )
        self.assertEqual(
            response.data["sao2"],
            [ErrorDetail(string="Ensure this value is greater than or equal to 30.", code="min_value")],
        )
        self.assertEqual(
            response.data["temperature"],
            [ErrorDetail(string="Ensure this value is less than or equal to 45.", code="max_value")],
        )
        self.assertEqual(
            response.data["glycemia"], [ErrorDetail(string="A valid integer is required.", code="invalid")]
        )
        self.assertEqual(
            response.data["gcs"],
            [ErrorDetail(string="Ensure this value is less than or equal to 15.", code="max_value")],
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
