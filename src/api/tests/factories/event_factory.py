from factory import Faker
from factory.django import DjangoModelFactory

from events.models import Event


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = Faker("first_name")
    description = Faker("sentence")
    localization = Faker("address")
