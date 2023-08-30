from factory.django import DjangoModelFactory
from faker import Factory, Faker

from events.models import Event

faker = Faker()


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = faker.first_name()
    description = faker.text()
    localization = faker.adress()
