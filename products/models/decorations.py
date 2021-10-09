from django.db import models
from .base import AbstractProduct, Category


class DecorationsProducts(AbstractProduct):
    class Meta:
        verbose_name = "Decoration Product"
        verbose_name_plural = "Decoration Products"

    decoration_product_type = models.ManyToManyField(
        Category,
        related_name="decoration_product_types",
        related_query_name="decoration_product_type",
    )