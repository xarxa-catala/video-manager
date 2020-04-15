"""
Django settings for VideoManager project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPGroupQuery
from .constants import *
try:
    from .settings_secret import *
except:
    print("Missing settings_secret.py file.")
    quit()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SECRET_KEY_SAVED

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['gestio.multimedia.xarxacatala.cat', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sortedm2m',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'VideoManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'VideoManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DATABASE_MYSQL,
        'USER': USER_NAME,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Authentication

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_LDAP_SERVER_URI = "ldap://ldap.xarxacatala.cat"
AUTH_LDAP_BIND_DN = "uid=multimedia,ou=serveis,dc=xarxacatala,dc=cat"
AUTH_LDAP_START_TLS = True
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=actius,dc=xarxacatala,dc=cat"
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "displayName",
    "email": "mail"
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=xarxacatala,dc=cat",
    ldap.SCOPE_SUBTREE,
    "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_REQUIRE_GROUP = (
    LDAPGroupQuery("cn=encodadors,ou=grups,dc=xarxacatala,dc=cat") |
    LDAPGroupQuery("cn=superadmin,ou=grups,dc=xarxacatala,dc=cat")
)
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=encodadors,ou=grups,dc=xarxacatala,dc=cat",
    "is_staff": "cn=encodadors,ou=grups,dc=xarxacatala,dc=cat",
    "is_superuser": "cn=superadmin,ou=grups,dc=xarxacatala,dc=cat"
}
# Mirror LDAP group assignments.
AUTH_LDAP_MIRROR_GROUPS = True
# For more granular permissions, we can map LDAP groups to Django groups.
AUTH_LDAP_FIND_GROUP_PERMS = True


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = STATIC_ROOT_SAVED

MEDIA_ROOT = MEDIA_ROOT_SAVED
MEDIA_URL = '/media/'
