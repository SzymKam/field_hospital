from json import dumps

from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.user_factory import UserFactory

fake = Faker()


class TestUserUpdateResponse(TestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory()
        self.user_2 = UserFactory()
        self.url_detail = reverse("api-user-update-detail", kwargs={"pk": self.user_1.id})
        self.headers = {"content_type": "application/json"}

    def test_detail_get_not_logged_user_return_403(self):
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_return_405(self):
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_have_permissions_return_405(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="view_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_post_not_logged_user_return_403(self):
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_no_permissions_return_403(self):
        self.client.force_login(user=self.user_1)

        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["detail"],
            ErrorDetail(string="You do not have permission to perform this action.", code="permission_denied"),
        )

    def test_detail_post_logged_user_have_permissions_return_405(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_patch_not_logged_user_return_403(self):
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_no_permissions_return_403(self):
        self.client.force_login(user=self.user_1)
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_delete_not_logged_user_return_403(self):
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_no_permissions_return_403(self):
        self.client.force_login(user=self.user_1)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_have_permissions_return_405(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="delete_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_patch_logged_user_have_permissions_invalid_id_return_404(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(reverse("api-user-update-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_have_permissions_return_200(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        data = {
            "username": fake.first_name(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
        }

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

        self.assertEqual(response.data["username"], data["username"])

    def test_detail_patch_logged_user_have_permissions_invalid_email_return_400(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        data = {"email": "invalid_email"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["email"], [ErrorDetail(string="Enter a valid email address.", code="invalid")])

    def test_detail_patch_logged_user_have_permissions_duplicated_email_return_400(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        data = {"email": self.user_2.email}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["email"], {"email": ErrorDetail(string="This email is already in use.", code="invalid")}
        )

    @tag("x")
    def test_detail_patch_logged_user_have_permissions_duplicated_username_return_400(self):
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        data = {"username": self.user_2.username}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["username"], [ErrorDetail(string="A user with that username already exists.", code="unique")]
        )
