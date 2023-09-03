import random

from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from treatment.constants import DRUG_DOSAGE_FORM, DRUGS, UNIT_CHOICES
from treatment.models.drug_model import Drug

from .treatment_factory import TreatmentFactory


class DrugFactory(DjangoModelFactory):
    class Meta:
        model = Drug

    name = random.choice(DRUGS)[0]
    dose = Faker("pyfloat", left_digits=2, right_digits=1, positive=True)
    unit = random.choice(UNIT_CHOICES)[0]
    dosage_form = random.choice(DRUG_DOSAGE_FORM)[0]
    treatment = SubFactory(TreatmentFactory)
