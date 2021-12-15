from django.db import models
from .base import AbstractProduct


class KitchenProducts(AbstractProduct):
    class Meta:
        verbose_name = "Kitchen"
        verbose_name_plural = "Kitchen"
