from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from .models import ProductImage
from django.conf import settings
import os
import boto3


@receiver(post_delete, sender=ProductImage)
def product_image_delete(sender, instance, **kwargs):
    if settings.DEBUG:
        if instance.image:
            # BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
            # FOLDER_NAME = os.path.dirname(instance.image.path)
            # print(instance.image.path)
            # s3_resource = boto3.resource("s3")
            # bucket = s3_resource.Bucket(BUCKET_NAME)
            # count = bucket.objects.filter(Prefix=FOLDER_NAME)
            instance.image.delete(save=False)
            # if len(list(count)) == 0:
            # bucket.objects.filter(Prefix=FOLDER_NAME).delete()

    # elif instance.image:
    #     if os.path.isfile(instance.image.path):
    #         imagedir = os.path.dirname(instance.image.path)
    #         os.remove(instance.image.path)
    #         if len(os.listdir(imagedir)) == 0:
    #             os.rmdir(imagedir)
