from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = "static"
    default_acl = "public-read"

    def __init__(self, *args, **kwargs):
        kwargs["bucket_name"] = settings.AWS_STATIC_BUCKET_NAME
        kwargs["custom_domain"] = settings.AWS_STATIC_CUSTOM_DOMAIN
        super(StaticStorage, self).__init__(*args, **kwargs)


class PublicMediaStorage(S3Boto3Storage):
    location = "media"
    default_acl = "public-read"
    file_overwrite = False
