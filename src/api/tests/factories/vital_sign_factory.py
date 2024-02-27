import random

from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from treatment.models.vital_sign_model import VitalSign

from .treatment_factory import TreatmentFactory

fake = Faker()


class VitalSignFactory(DjangoModelFactory):
    class Meta:
        model = VitalSign

    bp_sys = random.randint(1, 350)
    bp_dia = random.randint(1, 350)
    hr = random.randint(1, 350)
    sao2 = random.randint(30, 100)
    temperature = random.uniform(13.0, 45.0)
    glycemia = random.randint(1, 900)
    gcs = random.randint(3, 15)
    treatment = SubFactory(TreatmentFactory)
