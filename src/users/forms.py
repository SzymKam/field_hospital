from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User


class MyUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password",
            "email",
            "user_permissions",
        ]
        field_classes = {"username": UsernameField}
