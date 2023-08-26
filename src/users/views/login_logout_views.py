from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class StaffLogin(LoginView):
    """page for login into service"""

    template_name = "users/login.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital login"
        return context


class StaffLogout(LoginRequiredMixin, LogoutView):
    """user logout page"""

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital logout"
        return context
