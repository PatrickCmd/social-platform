from .base import *

import dj_database_url

DEBUG = config('DEBUG', cast=bool)

# DATABASES['default'] = dj_database_url.config(
#     default=config('DATABASE_URL')
# )

import django_heroku
django_heroku.settings(locals(), test_runner=False)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
