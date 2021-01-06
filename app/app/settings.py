from pathlib import Path
from decouple import config
from split_settings.tools import optional, include

ENV = config('DJANGO_ENV', default='prod')
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

include(
    'allowed_hosts.py',
    optional('allowed_hosts.{0}.py'.format(ENV)),
    'django_apps.py',
    'project_apps.py',
    optional('project_apps.{0}.py'.format(ENV)), # Environment specific applications
    'django_middleware.py',
    'project_middleware.py',
    optional('project_middleware.{0}.py'.format(ENV)),
    'templates.py',
    'database.py',
    'validation.py',
    'static.py',
    optional('local_settings.py'),
)
