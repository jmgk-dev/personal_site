import os
from datetime import date, timedelta

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jmgk.dev', 'www.jmgk.dev', '134.199.233.167']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Bugsnag
BUGSNAG = {
    'api_key': BUGSNAG_API_KEY,
    'project_root': '/path/to/your/app',
}
