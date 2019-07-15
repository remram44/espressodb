"""
Django settings for lattedb project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)

SETTINGS_FILE = os.path.join(ROOT_DIR, "settings.yaml")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

with open(SETTINGS_FILE, "r") as fin:
    _SETTINGS = yaml.safe_load(fin.read())
    SECRET_KEY = _SETTINGS["SECRET_KEY"]
    PROJECT_APPS = _SETTINGS["PROJECT_APPS"]


ALLOWED_HOSTS = []

READ_CONFIG = True

# Application definition

INSTALLED_APPS = PROJECT_APPS + [
    "lattedb.config",
    "django_tables2",
    "bootstrap4",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lattedb.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "config", "templates"),
            os.path.join(BASE_DIR, "correlator", "templates"),
            os.path.join(BASE_DIR, "documentation", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "lattedb.config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


if READ_CONFIG:
    with open(os.path.join(ROOT_DIR, "db-config.yaml"), "r") as fin:
        CONFIG = yaml.safe_load(fin.read())
    DATABASES = {"default": CONFIG}

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "base", "static"),
    os.path.join(BASE_DIR, "correlator", "static"),
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG" if DEBUG else "INFO",
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "main.commands": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "base": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
    },
}

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap-responsive.html"

GRAPH_MODELS = {
    "all_applications": True,
    "pygraphviz": True,
    "layout": "dot",
    "group_models": True,
    "hide_edge_labels": False,
    "exclude_models": [
        "Group",
        "AbstractUser",
        "LogEntry",
        "Permission",
        "ContentType",
        "Session",
        "AbstractBaseSession",
        "User",
        "Base",
    ],
    "output": "models.pdf",
}
