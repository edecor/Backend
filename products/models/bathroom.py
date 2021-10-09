from django.db import models
from .base import AbstractProduct, ProductImage, Category


class BathroomProducts(AbstractProduct):
    class Meta:
        verbose_name = "Bathroom Product"
        verbose_name_plural = "Bathroom Products"

    bathroom_product_type = models.ManyToManyField(
        Category,
        related_name="bathroom_product_types",
        related_query_name="bathroom_product_type",
    )
