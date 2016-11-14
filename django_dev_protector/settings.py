import os
from django.conf import settings

DIR_NAME = os.path.dirname(__file__)

PROTECT_STATUS_DEFAULT = False

PROTECT_STATUS_VARIABLE = 'PROTECT_STATUS_VARIABLE'
PROTECT_STATUS_FILE = '/protect_status.conf'

TEMPLATE_NAME = 'django_dev_protector/index.html' if not hasattr(settings, 'PROTECT_TEMPLATE_NAME') else settings.PROTECT_TEMPLATE_NAME

REDIRECT_URL = None if not hasattr(settings, 'PROTECT_REDIRECT_URL') else settings.PROTECT_REDIRECT_URL


from django_dev_protector.setup import get_status
os.environ[PROTECT_STATUS_VARIABLE] = get_status()
