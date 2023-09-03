from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from patients.models import Patient

from .event_factory import EventFactory


class PatientFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    name = Faker("first_name")
    surname = Faker("last_name")
    PESEL = Faker("pyint", min_value=10000000000, max_value=99999999999)
    address = Faker("address")
    phone = Faker("pyint", min_value=100000000, max_value=999999999)
    email = Faker("email")
    additional_info = Faker("sentence")
    event = SubFactory(EventFactory)
