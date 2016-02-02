import dj_database_url

from .base import *


DATABASES = {'default': dj_database_url.config()}

DEBUG = True

TEMPLATE_DEBUG = True