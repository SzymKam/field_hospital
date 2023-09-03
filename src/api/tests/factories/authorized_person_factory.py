from factory import Faker
from factory.django import DjangoModelFactory

from patients.models import AuthorizedPerson


class AuthorizedPersonFactory(DjangoModelFactory):
    class Meta:
        model = AuthorizedPerson

    name = Faker("first_name")
    surname = Faker("last_name")
    phone = Faker("random_int")
