from typing import Any

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class CreateUserView(CreateView):
    model = User
    template_name = "users/user-create.html"
    form_class = UserCreationForm
    queryset = User.objects.all()
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Create new user"
        return context


class ListUserView(ListView):
    template_name = "users/user-list.html"
    queryset = User.objects.all()

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "List of users"
        return context


class UpdateUserView(UpdateView):
    model = User
    template_name = "users/user-update.html"
    form_class = UserChangeForm
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Update User"
        return context

    # todo add permissions, login_url


class DeleteUserView(DeleteView):
    model = User
    template_name = "users/user-delete.html"
    success_url = reverse_lazy("user-list")

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete user"
        return context

    # todo add permissions, login_url
