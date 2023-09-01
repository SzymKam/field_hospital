from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Faker

from treatment.models.treatment_model import Treatment

from .medical_staff_factory import MedicalStaffFactory
from .patient_factory import PatientFactory

fake = Faker()


class TreatmentFactory(DjangoModelFactory):
    class Meta:
        model = Treatment

    interview = fake.text()
    description = fake.text()
    diagnosis = fake.name()
    medical_staff = SubFactory(MedicalStaffFactory)
    patient = SubFactory(PatientFactory)  # FK one to one
