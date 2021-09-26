from .base import *

# DEBUG = False
DEBUG = True

ALLOWED_HOSTS = [
    config("TEMP_EDECOR_DOMAIN"),
    config("AWS_EC2_IP"),
    config("AWS_EC2_PUBLIC_DNS"),
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
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

# STATIC_URL = "/static/"
# MEDIA_URL = "/media/"

# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# ---------------- REST FRAMEWORK ----------------

REST_FRAMEWORK = {
    **REST_FRAMEWORK,
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
}

# -------------- AWS ------------------

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = "public-read"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}

# s3 static settings
STATIC_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/"
STATICFILES_STORAGE = "core.storage_backends.StaticStorage"

# s3 public media settings
PUBLIC_MEDIA_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "core.storage_backends.PublicMediaStorage"
