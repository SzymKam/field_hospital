from django.urls import path

from .views.user_views import (
    CreateUserView,
    DeleteUserView,
    ListUserView,
    LoginView,
    LogoutView,
    UpdateUserView,
)

urlpatterns = [
    path(
        "create",
        CreateUserView.as_view(),
        name="user-create",
    ),
    path("list", ListUserView.as_view(), name="user-list"),
    path("update/<int:pk>", UpdateUserView.as_view(), name="user-update"),
    path("delete/<int:pk>", DeleteUserView.as_view(), name="user-delete"),
    path("login", LoginView.as_view(template_name="users/login.html"), name="user-login"),
    path("logout", LogoutView.as_view(), name="user-logout"),
]
