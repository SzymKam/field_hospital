from django.urls import path

from .views.login_logout_reset_views import StaffLogin, StaffLogout
from .views.user_views import (
    CreateUserView,
    DeleteUserView,
    ListUserView,
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
    path("login", StaffLogin.as_view(), name="user-login"),
    path("logout", StaffLogout.as_view(), name="user-logout"),
]
