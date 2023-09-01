from factory.django import DjangoModelFactory
from faker import Faker

from events.models import Event

fake = Faker()


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = fake.first_name()
    description = fake.text()
    localization = fake.address()
