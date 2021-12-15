from django.db import models
from .base import AbstractProduct


class HardwareToolProducts(AbstractProduct):
    class Meta:
        verbose_name = "Hardware and Tool"
        verbose_name_plural = "Hardware and Tool"
