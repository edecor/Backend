from django.db import models
from .base import AbstractProduct


class RugsMatFloorProducts(AbstractProduct):
    class Meta:
        verbose_name = "Rugs Mats and Floor"
        verbose_name_plural = "Rugs Mats and Floor"
