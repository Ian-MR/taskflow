# ruff: noqa: F403, F405

import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    host.strip() for host in os.environ["TASKFLOW_ALLOWED_HOSTS"].split(",") if host.strip()
]

MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {"BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"},
}

DATABASES["default"]["OPTIONS"] = {
    "sslmode": os.environ.get("TASKFLOW_DB_SSLMODE", "require"),
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = int(os.environ["TASKFLOW_SECURE_HSTS_SECONDS"])
