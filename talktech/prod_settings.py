from .settings import *
import dj_database_url

DEBUG = True
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['talktech.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'