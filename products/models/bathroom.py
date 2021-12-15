from django.db import models
from .base import AbstractProduct


class BathroomProducts(AbstractProduct):
    class Meta:
        verbose_name = "Bathroom Product"
        verbose_name_plural = "Bathroom Products"
