from typing import Any

from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)


class MyPasswordResetView(PasswordResetView):
    template_name = "users/password-reset.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital password reset"
        return context


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password-reset-sent.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital password reset sent"
        return context


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password-reset-done.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital password reset done"
        return context


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password-reset-form.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Hospital password reset confirm"
        return context
