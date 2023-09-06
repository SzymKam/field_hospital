from json import dumps

from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.exceptions import ErrorDetail

from ..factories.user_factory import UserFactory

fake = Faker()


class TestUserPasswordResetResponse(TestCase):
    def setUp(self) -> None:
        self.user_1 = UserFactory()
        self.user_2 = UserFactory(password="7ad998f32c65eeccb8ea")
        self.url_detail = reverse("api-user-password-reset-detail", kwargs={"pk": self.user_1.id})
        self.headers = {"content_type": "application/json"}

    def test_detail_get_not_logged_user_return_403(self) -> None:
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_get_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="view_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.get(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_detail_post_not_logged_user_return_403(self) -> None:
        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_detail_post_logged_user_no_permissions_return_403(self) -> None:
        self.client.force_login(user=self.user_1)

        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["detail"], ErrorDetail(string='Method "POST" not allowed.', code="method_not_allowed")
        )

    def test_detail_post_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="add_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.post(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(
            response.data["detail"], ErrorDetail(string='Method "POST" not allowed.', code="method_not_allowed")
        )

    def test_detail_patch_not_logged_user_return_403(self) -> None:
        response = self.client.patch(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_delete_not_logged_user_return_403(self) -> None:
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_no_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_delete_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="delete_user")
        self.user_1.user_permissions.add(self.permission)
        response = self.client.delete(path=self.url_detail)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_detail_patch_logged_user_have_permissions_invalid_id_return_404(self) -> None:
        self.client.force_login(user=self.user_1)
        self.permission = Permission.objects.get(codename="change_user")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(reverse("api-user-update-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_invalid_id_return_403(self) -> None:
        self.client.force_login(user=self.user_1)

        response = self.client.patch(reverse("api-user-update-detail", kwargs={"pk": 99999}))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_return_200(self) -> None:
        self.client.force_login(user=self.user_1)

        data = {"password": "kktjjywtyg5x", "password2": "kktjjywtyg5x"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_detail_patch_logged_user_invalid_password_2_return_400(self) -> None:
        self.client.force_login(user=self.user_1)

        data = {"password": "kktjjywtyg5x", "password2": "aaaaaaaa"}

        response = self.client.patch(path=self.url_detail, data=dumps(data), headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["password"], [ErrorDetail(string="Password fields didn't match.", code="invalid")]
        )

    def test_detail_patch_logged_user_invalid_old_password_return_400(self) -> None:
        self.client.force_login(user=self.user_2)

        data = {"password": "kktjjywtyg5x", "password2": "kktjjywtyg5x", "old_password": "aaaaaaaaaaaaa"}

        response = self.client.patch(
            reverse("api-user-password-reset-detail", kwargs={"pk": self.user_2.id}),
            data=dumps(data),
            headers=self.headers,
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(
            response.data["old_password"],
            {"old_password": ErrorDetail(string="Old password is not correct", code="invalid")},
        )

    # @tag('x')
    # def test_detail_patch_logged_user_valid_old_password_return_400(self) -> None:
    #     print(self.user_2.password)
    #     self.client.force_login(user=self.user_2)
    #
    #     data = {"password": 'kktjjywtyg5x',
    #             "password2": 'kktjjywtyg5x',
    #             'old_password': '7ad998f32c65eeccb8ea'}
    #     print(data['old_password'])
    #
    #     response = self.client.patch(reverse("api-user-password-reset-detail", kwargs={"pk": self.user_2.id}), data=dumps(data), headers=self.headers)
    #
    #     print(response.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
