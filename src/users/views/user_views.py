from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from ..forms import MyUserCreationForm, MyUserUpdateForm


class CreateUserView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "auth.add_user"
    permission_denied_message = "Only admins can create user"
    model = User
    template_name = "users/user-create.html"
    form_class = MyUserCreationForm
    queryset = User.objects.all()
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create new user"
        return context


class ListUserView(LoginRequiredMixin, ListView):
    template_name = "users/user-list.html"
    queryset = User.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "List of users"
        return context


class UpdateUserView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "auth.change_user"
    permission_denied_message = "Only admins can edit user"
    model = User
    template_name = "users/user-update.html"
    form_class = MyUserUpdateForm
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update User"
        return context


class DeleteUserView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "auth.delete_user"
    permission_denied_message = "Only admins can delete user"
    login_url = "all-events"

    model = User
    template_name = "users/user-delete.html"
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete user"
        return context
