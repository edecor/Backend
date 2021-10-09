from django.db import models
from .base import AbstractProduct, Category


class HardwareToolProducts(AbstractProduct):
    class Meta:
        verbose_name = "Hardware and Tool"
        verbose_name_plural = "Hardware and Tool"

    hardwaretool_product_type = models.ManyToManyField(
        Category,
        related_name="hardwaretool_product_types",
        related_query_name="hardwaretool_product_type",
    )
