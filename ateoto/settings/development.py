from ateoto.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SECRETS['dev_db_name'],
        'USER': SECRETS['dev_db_user'],
        'PASSWORD': SECRETS['dev_db_pass'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from local_settings import *
except:
    pass
