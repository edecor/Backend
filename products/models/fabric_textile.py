from django.db import models
from .base import AbstractProduct, Category


class FabricTextileProducts(AbstractProduct):
    class Meta:
        verbose_name = "Fabric and Textile Products"
        verbose_name_plural = "Fabric and Textile Products"

    fabrictextile_product_type = models.ManyToManyField(
        Category,
        related_name="fabrictextile_product_types",
        related_query_name="fabrictextile_product_type",
    )
