from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "password",
            "user_permissions",
            "username",
            "first_name",
            "last_name",
            "email",
        ]
        field_classes = {"username": UsernameField}
