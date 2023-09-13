import secrets

from django.contrib.auth.models import User
from factory import Faker
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = Faker("first_name")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    password = secrets.token_hex(nbytes=10)
