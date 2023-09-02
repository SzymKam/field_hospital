from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from patients.models import Patient

from .event_factory import EventFactory

fake = Faker()


class PatientFactory(DjangoModelFactory):
    class Meta:
        model = Patient

    name = fake.first_name()
    surname = fake.last_name()
    PESEL = fake.numerify(text="###########")
    address = fake.address()
    phone = fake.numerify(text="#########")
    email = fake.email()
    additional_info = fake.text()
    event = SubFactory(EventFactory)
