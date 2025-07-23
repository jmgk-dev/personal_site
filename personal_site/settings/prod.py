import os
from datetime import date, timedelta

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jmgk.dev', 'www.jmgk.dev', '134.199.233.167']

print("Using production settings")

SECRET_KEY = os.environ['DJANGO_SECURE_PRODUCTION_KEY']

# Bugsnag

BUGSNAG = {
    'api_key': os.environ['BUGSNAG_API_KEY'],
    'project_root': os.environ['PATH_TO_YOUR_APP'],
}

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/home/jamie/django_error.log',  # Change 'jamie' if your username is different
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}