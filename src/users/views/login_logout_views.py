from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class StaffLogin(LoginView):
    """page for login into service"""

    template_name = "users/login.html"
    extra_context = {"title": "Hospital login"}


class StaffLogout(LoginRequiredMixin, LogoutView):
    """user logout page"""

    extra_context = {"title": "Hospital logout"}
