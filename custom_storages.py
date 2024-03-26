from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# Code from Code Institute Boutique Ado Walksthrough
class StaticStorage(S3Boto3Storage):
    """Storage for static files in a specific S3 location."""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Storage for media files in a specific S3 location."""
    location = settings.MEDIAFILES_LOCATION