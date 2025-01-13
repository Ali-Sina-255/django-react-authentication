from decouple import config

from .base import *
from .base import env

SECRET_KEY = config(
    "DJANGO-SECRET_KEY",
    default="AuG1XPiMlZmrJ5UH0eo426fBPCPaz6gYWjzLAaq2vsngwXI0XhutooZKnf_th4wghOcAj5s6Jnus3vyR",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

ALLOWED_HOSTS = ["0.0.0.0", "localhost", "127.0.0.1"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "TETeam.@gmail.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "TET Team"
