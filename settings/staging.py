import dj_database_url

from .base import *


INSTALLED_APPS += ('storages',)

DATABASES = {'default': dj_database_url.config()}

DEBUG = True

TEMPLATE_DEBUG = True

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
               'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
               'Cache-Control': 'max-age=94608000',
}

AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_BUCKET_NAME')
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'