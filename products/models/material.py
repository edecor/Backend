from django.db import models
from .base import AbstractProduct, Category


class Material(AbstractProduct):
    PLACE_CHOICES = (
        ("INDOOR", "Indoor"),
        ("OUTDOOR", "Outdoor"),
        ("BOTH", "Both"),
    )
    MATERIAL_CATEGORY_CHOICES = (
        ("WALL", "Wall material"),
        ("CEILING", "Ceiling material"),
        ("FLOOR", "Floor material"),
    )

    material_place = models.CharField(max_length=15, choices=PLACE_CHOICES)
    material_category = models.CharField(
        max_length=7, choices=MATERIAL_CATEGORY_CHOICES
    )

    material_type = models.ManyToManyField(
        Category, related_name="material_types", related_query_name="material_type"
    )

    thickness = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    shape = models.CharField(max_length=50, blank=True)
    density = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Finish Material"
        verbose_name_plural = "Finish Materials"
