import dj_database_url
from .settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE +=['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = '@yb&tp72ydnre^jt&-72ag&m@85f&mlg0xa^u)^_5$wt1_3e%m'

ALLOWED_HOSTS = ['easy-isr.herokuapp.com']

