from django.db import models
from .base import AbstractProduct, ProductImage, Category


class FurnitureProducts(AbstractProduct):
    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural = "Furnitures"

    furniture_product_type = models.ManyToManyField(
        Category,
        related_name="furniture_product_types",
        related_query_name="furniture_product_type",
    )
