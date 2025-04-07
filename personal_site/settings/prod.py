import os
from datetime import date, timedelta

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['jmgk.dev', 'www.jmgk.dev', '134.199.233.167']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# Bugsnag

# BUGSNAG = {
#     'api_key': 'e67ab4514492f52ffdc0c60270c6af28',
#     'project_root': '/home/jamiek/kinorg',
# }
