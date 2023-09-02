from factory.django import DjangoModelFactory
from faker import Faker

from patients.models import AuthorizedPerson

fake = Faker()


class AuthorizedPersonFactory(DjangoModelFactory):
    class Meta:
        model = AuthorizedPerson

    name = fake.first_name()
    surname = fake.last_name()
    phone = fake.numerify(text="#########")
