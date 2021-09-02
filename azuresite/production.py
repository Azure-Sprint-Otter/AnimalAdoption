import os
from .settings import *

if 'WEBSITE_HOSTNAME' in os.environ:
    ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
else:
    ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taa_portal',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'psql-aap-dev-sea-001.postgres.database.azure.com',
        'PORT': '5432',
    },
}

MIDDLEWARE = [                                                                   
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'adoptionsite.apps.AdoptionsiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'