from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status

from api.tests.factories.user_factory import UserFactory


class UserLogoutTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserFactory()
        self.url = reverse("user-logout")

    def test_get_not_logged_user_return_302(self) -> None:
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_302(self) -> None:
        self.client.force_login(self.user)
        response = self.client.get(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
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

    def test_delete_logged_user_return_405(self) -> None:
        self.client.force_login(self.user)
        response = self.client.delete(path=self.url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
