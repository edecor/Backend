from django.db import models
from .base import AbstractProduct


class LightProducts(AbstractProduct):
    class Meta:
        verbose_name = "Light"
        verbose_name_plural = "Lights"
