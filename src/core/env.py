import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, get_random_secret_key()),
    USER=(str, "db_field_hospital"),
    PASSWORD=(str, "db_field_hospital"),
    NAME=(str, "db_field_hospital"),
    HOST=(str, "db"),
    EMAIL_HOST_PASSWORD=(str, None),
    EMAIL_HOST_USER=(str, None),
    DEFAULT_FROM_EMAIL=(str, None),
)
