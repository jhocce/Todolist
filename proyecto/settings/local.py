from .base import *

DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'proyecto.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS= [BASE_DIR.child("templates")]

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'tareas/tareas'

AUTH_USER_MODEL = 'user.User'


STATIC_FILES = [BASE_DIR.child('static')]

STATICFILES_DIRS = [BASE_DIR.child('static')]