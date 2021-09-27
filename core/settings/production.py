from .base import *

DEBUG = False
# DEBUG = True

ALLOWED_HOSTS = [
    config("TEMP_EDECOR_DOMAIN"),
    config("AWS_EC2_IP"),
    config("AWS_EC2_PUBLIC_DNS"),
    "edecor.com.bd",
    "www.edecor.com.bd",
    "localhost",
    "127.0.0.1",
    "0.0.0.0",
]

MIDDLEWARE += [
    "csp.middleware.CSPMiddleware",
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
    "https://media.edecor.com.bd",
    "https://static.edecor.com.bd",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
if not DEBUG:
    SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSP_SCRIPT_SRC = ("'self'", "media.edecor.com.bd", "https://static.edecor.com.bd")
CSP_IMG_SRC = ("'self'", "media.edecor.com.bd", "https://static.edecor.com.bd")
CSP_FONT_SRC = ("'self'", "media.edecor.com.bd", "https://static.edecor.com.bd")
CSP_STYLE_SRC = ("'self'", "media.edecor.com.bd", "https://static.edecor.com.bd")
CSP_DEFAULT_SRC = ("'none'",)

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

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
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_CUSTOM_DOMAIN = "media.edecor.com.bd"


# s3 static settings
AWS_STATIC_BUCKET_NAME = config("AWS_STATIC_BUCKET_NAME")
AWS_STATIC_CUSTOM_DOMAIN = config("AWS_STATIC_CUSTOM_DOMAIN")
STATIC_URL = "https://static.edecor.com.bd/"
STATICFILES_STORAGE = "core.storage_backends.StaticStorage"

# s3 public media settings
MEDIA_URL = "https://media.edecor.com.bd/"
DEFAULT_FILE_STORAGE = "core.storage_backends.PublicMediaStorage"
