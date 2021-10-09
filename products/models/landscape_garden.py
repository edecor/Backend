from django.db import models
from .base import AbstractProduct, Category


class LandscapeProducts(AbstractProduct):
    class Meta:
        verbose_name = "Landscape and Garden"
        verbose_name_plural = "Landscape and Garden"

    landscape_product_type = models.ManyToManyField(
        Category,
        related_name="landscape_product_types",
        related_query_name="landscape_product_type",
    )
