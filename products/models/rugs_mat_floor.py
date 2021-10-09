from django.db import models
from .base import AbstractProduct, Category


class RugsMatFloorProducts(AbstractProduct):
    class Meta:
        verbose_name = "Rugs Mats and Floor"
        verbose_name_plural = "Rugs Mats and Floor"

    rugmatfloor_product_type = models.ManyToManyField(
        Category,
        related_name="rugmatfloor_product_types",
        related_query_name="rugmatfloor_product_type",
    )
