from factory.django import DjangoModelFactory
from faker import Faker

from treatment.models.medical_staff_model import MedicalStaff

fake = Faker()


class MedicalStaffFactory(DjangoModelFactory):
    class Meta:
        model = MedicalStaff

    name = fake.first_name()
    surname = fake.last_name()
