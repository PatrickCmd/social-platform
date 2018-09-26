from .base import *

DEBUG = config('DEBUG', cast=bool)

INSTALLED_APPS += ['django_extensions']