from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.utils.encoding import force_str


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION