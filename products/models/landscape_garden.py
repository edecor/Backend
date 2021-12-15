from django.db import models
from .base import AbstractProduct


class LandscapeProducts(AbstractProduct):
    class Meta:
        verbose_name = "Landscape and Garden"
        verbose_name_plural = "Landscape and Garden"
