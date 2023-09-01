from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from faker import Faker

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = fake.first_name()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
