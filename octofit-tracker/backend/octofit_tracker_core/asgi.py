"""
ASGI config for octofit_tracker_core project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker_core.settings')

application = get_asgi_application()
