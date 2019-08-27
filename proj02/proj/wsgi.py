from __future__ import absolute_import, unicode_literals

import os

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application  # noqa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
