from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    # config("DOMAIN_NAME")
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "[::1]",
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("PRODUCTION_POSTGRES_DB"),
        "USER": config("PRODUCTION_POSTGRES_USER"),
        "PASSWORD": config("PRODUCTION_POSTGRES_PASSWORD"),
        "HOST": config("PRODUCTION_POSTGRES_HOST"),
        "PORT": config("PRODUCTION_POSTGRES_PORT"),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]
