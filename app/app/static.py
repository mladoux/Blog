from pathlib import os

STATIC_URL = '/static/'

#Location of static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')
