from django.contrib.auth.models import User
from factory.django import DjangoModelFactory
from faker import Factory, Faker

faker = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = faker.first_name()
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
