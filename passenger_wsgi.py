import os
import sys

sys.path.insert(0, os.path.join(os.environ['HOME'], 'mysite'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ['DJANGO_DEBUG'] = 'False'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'gandicap.hyz,www.gandicap.hyz'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
