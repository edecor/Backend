from django.db import models
from .base import AbstractProduct


class FurnitureProducts(AbstractProduct):
    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural = "Furnitures"
