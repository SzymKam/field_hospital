from factory import Faker
from factory.django import DjangoModelFactory

from treatment.models.medical_staff_model import MedicalStaff


class MedicalStaffFactory(DjangoModelFactory):
    class Meta:
        model = MedicalStaff

    name = Faker("first_name")
    surname = Faker("last_name")
