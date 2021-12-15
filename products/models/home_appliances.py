from django.db import models
from .base import AbstractProduct


class HomeApplianceProducts(AbstractProduct):
    class Meta:
        verbose_name = "Home Appliance"
        verbose_name_plural = "Home Appliances"
