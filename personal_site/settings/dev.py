import os
from datetime import date, timedelta

from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

if os.environ.get('RUN_MAIN') != 'true':
    print("Using development settings")

SECRET_KEY = os.getenv(
    'DJANGO_DEV_KEY',  
    'django-insecure-default-key-for-dev-only'
)


