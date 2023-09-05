# """/api/user-password-reset/<pk>/	api.views.user_view.ChangePasswordUserView	api-user-password-reset-detail
# /api/user-update/<pk>/	api.views.user_view.UpdateUserView	api-user-update-detail
# """
#
#
# from json import dumps
#
# from django.contrib.auth.models import Permission
# from django.test import TestCase, tag
# from django.urls import reverse
# from faker import Faker
# from rest_framework import status
# from rest_framework.exceptions import ErrorDetail
#
# from ..factories.user_factory import UserFactory
#
# fake = Faker()
#
#
# class TestUserUpdateResponse(TestCase):
#     def setUp(self) -> None:
#         self.user_1 = UserFactory()
#         self.user_2 = UserFactory()
#         self.url_detail = reverse("api-user-update-detail", kwargs={"pk": self.user_1.id})
#         self.headers = {"content_type": "application/json"}
#
#     @tag('x')
#     def test_detail_get_not_logged_user_return_403(self):
#         response = self.client.get(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "GET")
#         self.assertEqual(len(response.data), 1)
#
#     @tag('x')
#     def test_detail_get_logged_user_return_405(self):
#         self.client.force_login(user=self.user_1)
#         response = self.client.get(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "GET")
#         self.assertEqual(len(response.data), 1)
#
#     @tag('x')
#     def test_detail_get_logged_user_have_permissions_return_405(self):
#         self.client.force_login(user=self.user_1)
#         self.permission = Permission.objects.get(codename="view_user")
#         self.user_1.user_permissions.add(self.permission)
#         response = self.client.get(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "GET")
#         self.assertEqual(len(response.data), 1)
#
#     @tag('x')
#     def test_detail_post_not_logged_user_return_403(self):
#         response = self.client.post(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "POST")
#
#     @tag('x')
#     def test_detail_post_logged_user_no_permissions_return_403(self):
#         self.client.force_login(user=self.user_1)
#
#         response = self.client.post(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "POST")
#         self.assertEqual(
#             response.data["detail"],
#             ErrorDetail(string="You do not have permission to perform this action.", code="permission_denied"),
#         )
#
#     @tag('x')
#     def test_detail_post_logged_user_have_permissions_return_405(self):
#         self.client.force_login(user=self.user_1)
#         self.permission = Permission.objects.get(codename="add_user")
#         self.user_1.user_permissions.add(self.permission)
#
#         response = self.client.post(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "POST")
#
#     @tag('x')
#     def test_detail_patch_not_logged_user_return_403(self):
#         response = self.client.patch(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
#
#     @tag('x')
#     def test_detail_patch_logged_user_no_permissions_return_403(self):
#         self.client.force_login(user=self.user_1)
#         response = self.client.patch(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
#
#     @tag('x')
#     def test_detail_delete_not_logged_user_return_403(self):
#         response = self.client.delete(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
#
#     @tag('x')
#     def test_detail_delete_logged_user_no_permissions_return_403(self):
#         self.client.force_login(user=self.user_1)
#         response = self.client.delete(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
#
#     @tag('x')
#     def test_detail_delete_logged_user_have_permissions_return_405(self):
#         self.client.force_login(user=self.user_1)
#         self.permission = Permission.objects.get(codename="delete_user")
#         self.user_1.user_permissions.add(self.permission)
#         response = self.client.delete(path=self.url_detail)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
