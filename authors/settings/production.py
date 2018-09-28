import django_heroku

from .base import *

import dj_database_url

DEBUG = config('DEBUG', cast=bool)
django_heroku.settings(locals(), test_runner=False)

DATABASES['default'] = dj_database_url.config(
    default=config('DATABASE_URL')
)