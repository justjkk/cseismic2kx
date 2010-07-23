import os, sys

ROOTDIR = os.path.join(os.path.dirname(__file__), '..')
BASE_DIR = os.path.join(os.path.dirname(__file__), '../..')
sys.path.append(ROOTDIR)
sys.path.append(BASE_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'cseismic2kx.settings'

ROOTDIR = os.path.join(os.path.dirname(__file__), '..')

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
