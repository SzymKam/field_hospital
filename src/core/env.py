import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, get_random_secret_key()),
    USER=(str, "field_hospital_user"),
    PASSWORD=(str, "field_hospital_user"),
    HOST=(str, "db"),
)
