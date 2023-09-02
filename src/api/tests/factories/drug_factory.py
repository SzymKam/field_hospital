import random

from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from treatment.constants import DRUG_DOSAGE_FORM, DRUGS, UNIT_CHOICES
from treatment.models.drug_model import Drug

from .treatment_factory import TreatmentFactory

fake = Faker()


class DrugFactory(DjangoModelFactory):
    class Meta:
        model = Drug

    name = random.choice(DRUGS)[0]
    dose = fake.pyfloat()
    unit = random.choice(UNIT_CHOICES)[0]
    dosage_form = random.choice(DRUG_DOSAGE_FORM)[0]
    treatment = SubFactory(TreatmentFactory)
