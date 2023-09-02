from json import dumps

from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.authorized_person_factory import AuthorizedPersonFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class TestAuthorizedPersonResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.auth_person_1 = AuthorizedPersonFactory()
        self.auth_person_2 = AuthorizedPersonFactory()
        self.url_list = reverse("api-authorized-person-list")
        self.url_detail = reverse("api-authorized-person-detail", kwargs={"pk": self.auth_person_1.id})

        self.data = {"name": fake.first_name(), "surname": fake.last_name(), "phone": fake.numerify(text="#########")}
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

        self.assertEqual(response.data[0]["name"], self.auth_person_1.name)
        self.assertEqual(response.data[0]["surname"], self.auth_person_1.surname)
        self.assertEqual(response.data[0]["phone"], int(self.auth_person_1.phone))

        self.assertEqual(response.data[1]["name"], self.auth_person_2.name)
        self.assertEqual(response.data[1]["surname"], self.auth_person_2.surname)
        self.assertEqual(response.data[1]["phone"], int(self.auth_person_2.phone))

    def test_list_post_not_logged_user_return_403(self):
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_return_201(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.url_list, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["surname"], self.data["surname"])
        self.assertEqual(response.data["phone"], int(self.data["phone"]))

    def test_list_post_logged_user_post_str_number_instead_of_int_return_400(self):
        self.client.force_login(user=self.user)
        self.data.update({"phone": "itsaphonenumber"})
        response = self.client.post(path=self.url_list, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["phone"], [ErrorDetail(string="A valid integer is required.", code="invalid")])

    def test_list_post_logged_user_too_long_value_return_400(self):
        self.client.force_login(user=self.user)
        self.data.update({"name": fake.text()})
        response = self.client.post(path=self.url_list, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["name"],
            [ErrorDetail(string="Ensure this field has no more than 50 characters.", code="max_length")],
        )

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
        self.assertEqual(response.data["id"], self.auth_person_1.id)
        self.assertEqual(response.data["name"], self.auth_person_1.name)
        self.assertEqual(response.data["surname"], self.auth_person_1.surname)
        self.assertEqual(response.data["phone"], int(self.auth_person_1.phone))

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

        data = {"name": "updated_name"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), **self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["id"], self.auth_person_1.id)
        self.assertEqual(response.data["name"], data["name"])

    def test_detail_patch_logged_user_invalid_data_return_400(self):
        self.client.force_login(user=self.user)

        data = {"phone": "itsanumber"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), **self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["phone"], [ErrorDetail(string="A valid integer is required.", code="invalid")])

    def test_detail_patch_logged_user_invalid_id_return_404(self):
        self.client.force_login(user=self.user)

        response = self.client.patch(path=reverse("api-event-detail", kwargs={"pk": 99999}), **self.headers)

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
