import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from django.urls import reverse
from faker import Faker
from rest_framework import status

from ..factories.event_factory import EventFactory
from ..factories.user_factory import UserFactory

fake = Faker()


class TestEventResponse(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.event_1 = EventFactory()
        self.event_2 = EventFactory()
        self.url = reverse("api-event-list")
        self.data = {
            "name": fake.name(),
            "status": "Preparing",
            "description": fake.text(),
            "localization": fake.address(),
        }
        # self.url_detail = reverse("api-event-detail", kwargs={'id': 'id'})

    def test_get_not_logged_user_return_403(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 1)

    def test_get_logged_user_return_right_values_with_two_objects(self):
        self.client.force_login(user=self.user)
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0]["name"], self.event_1.name)
        self.assertEqual(response.data[0]["localization"], self.event_1.localization)
        self.assertEqual(response.data[0]["description"], self.event_1.description)

        self.assertEqual(response.data[1]["name"], self.event_2.name)
        self.assertEqual(response.data[1]["localization"], self.event_2.localization)
        self.assertEqual(response.data[1]["description"], self.event_2.description)

    def test_post_not_logged_user_return_403(self):
        response = self.client.post(path=self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_201(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.url, data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["description"], self.data["description"])
        self.assertEqual(response.data["status"], self.data["status"])
        self.assertEqual(response.data["localization"], self.data["localization"])

    def test_post_logged_user_invalid_status_return(self):
        self.client.force_login(user=self.user)
        response = self.client.post(path=self.url, data=self.data.update({"status": "any_status"}))

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data[0], "Invalid status")
