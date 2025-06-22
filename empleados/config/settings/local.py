from .base import *

DEBUG = True
ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# 
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'DBempleado1',
'USER': 'juli',
'PASSWORD': '9546',
'HOST': 'localhost',
'PORT': '5432',
}
}
STATIC_URL = 'static/'
