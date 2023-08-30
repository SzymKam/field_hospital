from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    UsernameField,
    ValidationError,
)
from django.contrib.auth.models import User
from django.forms import CharField, EmailField


class MyUserCreationForm(UserCreationForm):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(
        required=True,
        max_length=100,
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "user_permissions"]
        field_classes = {"username": UsernameField}

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email


class MyUserUpdateForm(UserChangeForm):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(required=True, max_length=100)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "user_permissions"]
        field_classes = {"username": UsernameField}

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email
