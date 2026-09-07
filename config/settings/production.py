# ruff: noqa: F403, F405

import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    host.strip() for host in os.environ["TASKFLOW_ALLOWED_HOSTS"].split(",") if host.strip()
]

STATIC_ROOT = BASE_DIR / "staticfiles"

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = int(os.environ["TASKFLOW_SECURE_HSTS_SECONDS"])
