from django.db import models
from .base import AbstractProduct


class FabricTextileProducts(AbstractProduct):
    class Meta:
        verbose_name = "Fabric and Textile"
        verbose_name_plural = "Fabric and Textile"
