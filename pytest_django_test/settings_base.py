import os

import django

ROOT_URLCONF = "pytest_django_test.urls"
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "pytest_django_test.app",
]

STATIC_URL = "/static/"
SECRET_KEY = "foobar"

# Used to construct unique test database names to allow detox to run multiple
# versions at the same time
db_suffix = "_%s" % os.getuid()

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

if django.VERSION < (1, 10):
    MIDDLEWARE_CLASSES = MIDDLEWARE


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    }
]
