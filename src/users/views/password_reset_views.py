from typing import Any

from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)


class MyPasswordResetView(PasswordResetView):
    template_name = "users/password-reset.html"
    extra_context = {"title": "Hospital password reset"}


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password-reset-sent.html"
    extra_context = {"title": "Hospital password reset sent"}


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password-reset-done.html"
    extra_context = {"title": "Hospital password reset done"}


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password-reset-form.html"
    extra_context = {"title": "Hospital password reset confirm"}
