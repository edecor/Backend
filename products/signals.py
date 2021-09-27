from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from .models import ProductImage
from django.conf import settings
import os
import boto3


@receiver(post_delete, sender=ProductImage)
def product_image_delete(sender, instance, **kwargs):
    if not settings.DEBUG:
        if instance.image:
            instance.image.delete(save=False)

    elif instance.image:
        if os.path.isfile(instance.image.path):
            imagedir = os.path.dirname(instance.image.path)
            os.remove(instance.image.path)
            if len(os.listdir(imagedir)) == 0:
                os.rmdir(imagedir)
