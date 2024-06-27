# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2555296/data/www/fezwer.ru/shelterShop')
sys.path.insert(1, '/var/www/u2555296/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shelterShop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()