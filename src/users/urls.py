from django.urls import path

from .views.login_logout_views import StaffLogin, StaffLogout
from .views.password_reset_views import (
    MyPasswordResetCompleteView,
    MyPasswordResetConfirmView,
    MyPasswordResetDoneView,
    MyPasswordResetView,
)
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
    path("reset_password/", MyPasswordResetView.as_view(), name="reset-password"),
    path(
        "reset_password_sent/",
        MyPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        MyPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        MyPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
