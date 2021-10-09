from django.db import models
from .base import AbstractProduct, Category


class LightProducts(AbstractProduct):
    class Meta:
        verbose_name = "Light"
        verbose_name_plural = "Lights"

    light_product_type = models.ManyToManyField(
        Category,
        related_name="light_product_types",
        related_query_name="light_product_type",
    )
