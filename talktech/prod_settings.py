from .settings import *
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = 't5rdh@nl4vgq*bw=88fut6n1rz2gih&r$5m@irl*go=g8#9xm7'

ALLOWED_HOSTS = ['talktech.herokuapp.com']

DATABASES['default'] = dj_database_url.config()