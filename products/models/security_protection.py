from django.db import models
from .base import AbstractProduct


class SecurityProtectionProducts(AbstractProduct):
    class Meta:
        verbose_name = "Security and Protection"
        verbose_name_plural = "Security and Protection"
