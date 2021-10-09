from django.db import models
from .base import AbstractProduct, Category


class SecurityProtectionProducts(AbstractProduct):
    class Meta:
        verbose_name = "Security and Protection"
        verbose_name_plural = "Security and Protection"

    securityprotection_product_type = models.ManyToManyField(
        Category,
        related_name="securityprotection_product_types",
        related_query_name="securityprotection_product_type",
    )
