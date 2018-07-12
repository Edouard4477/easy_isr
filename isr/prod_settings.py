import dj_database_url
from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

SECRET_KEY = '@yb&tp72ydnre^jt&-72ag&m@85f&mlg0xa^u)^_5$wt1_3e%m'

ALLOWED_HOSTS = ['easy-isr.herokuapp.com']

