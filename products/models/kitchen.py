from django.db import models
from .base import AbstractProduct, Category


class KitchenProducts(AbstractProduct):
    class Meta:
        verbose_name = "Kitchen Product"
        verbose_name_plural = "Kitchen Products"

    kitchen_product_type = models.ManyToManyField(
        Category,
        related_name="kitchen_product_types",
        related_query_name="kitchen_product_type",
    )
