from django.db import models
from .base import AbstractProduct


class DecorationsProducts(AbstractProduct):
    class Meta:
        verbose_name = "Decoration"
        verbose_name_plural = "Decoration"
