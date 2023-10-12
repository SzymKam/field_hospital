from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from treatment.models.treatment_model import Treatment

from .medical_staff_factory import MedicalStaffFactory


class TreatmentFactory(DjangoModelFactory):
    class Meta:
        model = Treatment

    interview = Faker("sentence")
    description = Faker("sentence")
    diagnosis = Faker("word")
    medical_staff = SubFactory(MedicalStaffFactory)
