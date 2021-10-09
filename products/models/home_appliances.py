from django.db import models
from .base import AbstractProduct, Category


class HomeApplianceProducts(AbstractProduct):
    class Meta:
        verbose_name = "Home Appliance Product"
        verbose_name_plural = "Home Appliance Products"

    homeappliance_product_type = models.ManyToManyField(
        Category,
        related_name="homeappliance_product_types",
        related_query_name="homeappliance_product_type",
    )
