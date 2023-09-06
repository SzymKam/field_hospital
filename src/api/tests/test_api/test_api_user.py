import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.user_factory import UserFactory

fake = Faker()


class TestUserResponse(TestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()
        self.url_list = reverse("api-user-list")
        self.url_detail = reverse("api-user-detail", kwargs={"pk": self.user_1.id})
        self.headers = {"content_type": "application/json"}
        self.password = secrets.token_hex(nbytes=10)

    def test_list_get_not_logged_user_return_403(self) -> None:
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_list_get_logged_user_return_right_values_with_two_objects_200(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["id"], self.user_1.id)
        self.assertEqual(response.data[0]["username"], self.user_1.username)
        self.assertEqual(response.data[0]["first_name"], self.user_1.first_name)
        self.assertEqual(response.data[0]["last_name"], self.user_1.last_name)
        self.assertEqual(response.data[0]["email"], self.user_1.email)

        self.assertEqual(response.data[1]["id"], self.user_2.id)
        self.assertEqual(response.data[1]["username"], self.user_2.username)
        self.assertEqual(response.data[1]["first_name"], self.user_2.first_name)
        self.assertEqual(response.data[1]["last_name"], self.user_2.last_name)
        self.assertEqual(response.data[1]["email"], self.user_2.email)

    def test_list_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_list_post_logged_user_no_permissions_return_403(self) -> None:
        self.client.force_login(user=self.user_1)

        response = self.client.post(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["detail"],
            ErrorDetail(string="You do not have permission to perform this action.", code="permission_denied"),
        )

    def test_list_post_logged_user_have_permissions_return_201(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": fake.first_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": self.password,
            "password2": self.password,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

        self.assertEqual(response.data["username"], data["username"])
        self.assertEqual(response.data["first_name"], data["first_name"])
        self.assertEqual(response.data["last_name"], data["last_name"])
        self.assertEqual(response.data["email"], data["email"])

    def test_list_post_logged_user_have_permissions_invalid_value_return_400(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": self.user_2.username,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": "email",
            "password": self.password,
            "password2": self.password,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["username"], [ErrorDetail(string="This field must be unique.", code="unique")])
        self.assertEqual(response.data["email"], [ErrorDetail(string="Enter a valid email address.", code="invalid")])

    def test_list_post_logged_user_have_permissions_invalid_password1_return_400(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": fake.first_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": self.password,
            "password2": "password2",
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["password"], [ErrorDetail(string="Password fields didn't match.", code="invalid")]
        )

    def test_list_post_logged_user_have_permissions_commom_password_return_400(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": fake.first_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": "password",
            "password2": self.password,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["password"], [ErrorDetail(string="This password is too common.", code="password_too_common")]
        )

    def test_list_post_logged_user_have_permissions_invalid_password2_return_400(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": fake.first_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": secrets.token_hex(nbytes=10),
            "password2": self.password,
        }
        response = self.client.post(path=self.url_list, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["password"], [ErrorDetail(string="Password fields didn't match.", code="invalid")]
        )

    def test_list_patch_not_logged_user_return_403(self) -> None:
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_patch_logged_user_no_permissions_return_403(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_patch_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.patch(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_list_delete_not_logged_user_return_403(self) -> None:
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_list_delete_logged_user_no_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_list_delete_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="delete_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.delete(path=self.url_list)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_get_not_logged_user_return_403(self) -> None:
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_return_right_values_200(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

        self.assertEqual(response.data["id"], self.user_1.id)
        self.assertEqual(response.data["username"], self.user_1.username)
        self.assertEqual(response.data["first_name"], self.user_1.first_name)
        self.assertEqual(response.data["last_name"], self.user_1.last_name)
        self.assertEqual(response.data["email"], self.user_1.email)

    def test_detail_get_logged_user_invalid_id_return_error_404(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.get(reverse("api-user-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_detail_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_no_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_patch_not_logged_user_return_403(self) -> None:
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_no_permissions_return_403(self) -> None:
        self.client.force_login(user=self.user_1)

        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["detail"],
            ErrorDetail(string="You do not have permission to perform this action.", code="permission_denied"),
        )

    def test_detail_patch_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["detail"], ErrorDetail(string='Method "PATCH" not allowed.', code="method_not_allowed")
        )

    def test_detail_patch_logged_user_have_permissions_invalid_id_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(reverse("api-user-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["detail"], ErrorDetail(string='Method "PATCH" not allowed.', code="method_not_allowed")
        )

    def test_detail_delete_not_logged_user_return_403(self) -> None:
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_no_permissions_return_403(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_have_permissions_return_204(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="delete_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_have_permissions_invalid_id_return_404(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="delete_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.delete(reverse("api-user-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
