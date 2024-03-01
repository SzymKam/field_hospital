import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, get_random_secret_key()),
    DB_USER=(str, "db_field_hospital"),
    DB_PASSWORD=(str, "db_field_hospital"),
    DB_NAME=(str, "db_field_hospital"),
    DB_HOST=(str, "db"),
    EMAIL_HOST_PASSWORD=(str, None),
    EMAIL_HOST_USER=(str, None),
    DEFAULT_FROM_EMAIL=(str, None),
    USE_RDS=(bool, False),
    USE_S3=(bool, False),
)
