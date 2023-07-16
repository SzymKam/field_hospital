import environ
from django.core.management.utils import get_random_secret_key

env = environ.Env(
    DEBUG=(bool, True),
    # SECRET_KEY=(str, get_random_secret_key()),
    SECRET_KEY=(
        str,
        "django-insecure-%9nd24mrhy$8vgm2s5pga%h_^quy^xmxr^khbo_^s8zokuv1ky",
    ),
    MYPY_DJANGO_CONFIG=(str, "./mypy.ini"),
)
