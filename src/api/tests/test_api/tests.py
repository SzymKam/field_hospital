# class TestBIGResponse(TestCase):
#
#     def test_post_logged_have_permissions_user_return_405(self):
#         url = reverse("big-list")
#         self.client.force_login(self.user)
#         self.permission = Permission.objects.get(codename="add_big")
#         self.user.user_permissions.add(self.permission)
#
#         response = self.client.post(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "POST")
#
#
#
#     def test_post_not_logged_user_return_403(self):
#         url = reverse("big-list")
#
#         response = self.client.post(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "POST")
#
#     def test_patch_logged_have_permissions_user_return_405(self):
#         url = reverse("big-list")
#
#         self.client.force_login(self.user)
#         self.permission = Permission.objects.get(codename="change_big")
#         self.user.user_permissions.add(self.permission)
#
#         response = self.client.patch(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
#
#     def test_patch_logged_user_no_permissions_return_403(self):
#         url = reverse("big-list")
#         self.client.force_login(self.user)
#
#         response = self.client.patch(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
#
#     def test_patch_not_logged_user_return_403(self):
#         url = reverse("big-list")
#         response = self.client.patch(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
#
#     def test_delete_logged_have_permissions_user_return_405(self):
#         url = reverse("big-list")
#
#         self.client.force_login(self.user)
#         self.permission = Permission.objects.get(codename="delete_big")
#         self.user.user_permissions.add(self.permission)
#
#         response = self.client.delete(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
#
#     def test_delete_logged_user_no_permissions_return_403(self):
#         url = reverse("big-list")
#         self.client.force_login(self.user)
#
#         response = self.client.delete(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
#
#     def test_delete_not_logged_user_return_403(self):
#         url = reverse("big-list")
#         response = self.client.delete(path=url)
#
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
