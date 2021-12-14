import functools
import operator

from .material import Material
from .bathroom import BathroomProducts
from .decorations import DecorationsProducts
from .fabric_textile import FabricTextileProducts
from .furniture import FurnitureProducts
from .hardware_tool import HardwareToolProducts
from .home_appliances import HomeApplianceProducts
from .kitchen import KitchenProducts
from .landscape_garden import LandscapeProducts
from .light import LightProducts
from .rugs_mat_floor import RugsMatFloorProducts
from .security_protection import SecurityProtectionProducts

from django.db import models
from django.db.models import Q
from django.db.models.constraints import CheckConstraint

from versatileimagefield.fields import VersatileImageField

# JUST TESTING WITH only "material" model need to add support dynamically
def return_product_image_directory(instance, filename):
    if instance.is_description_image:
        return f"products/{instance.material.slug}/description/{filename}"
    return f"products/{instance.material.slug}/main/{filename}"


def checkImageOwner(name):
    q_objs = []
    all_field_names = [
        "material",
        "bathroom",
        "decorations",
        "furniture",
        "fabric_textile",
        "hardware_tool",
        "home_appliances",
        "kitchen",
        "landscape_garden",
        "light",
        "rugs_mat",
        "security_protection",
    ]

    for field_name in all_field_names:
        q_obj = Q(
            **{
                f"{f_name}__isnull": (False if field_name == f_name else True)
                for f_name in all_field_names
            }
        )
        q_objs.append(q_obj)

    return CheckConstraint(check=functools.reduce(operator.or_, q_objs), name=name)


class ProductImage(models.Model):

    image = VersatileImageField(
        upload_to=return_product_image_directory,
        max_length=600,
    )
    alt = models.CharField(max_length=128)
    is_description_image = models.BooleanField(default=False)

    material = models.ForeignKey(
        Material, on_delete=models.CASCADE, blank=True, null=True
    )
    bathroom = models.ForeignKey(
        BathroomProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    decorations = models.ForeignKey(
        DecorationsProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    furniture = models.ForeignKey(
        FurnitureProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    fabric_textile = models.ForeignKey(
        FabricTextileProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    hardware_tool = models.ForeignKey(
        HardwareToolProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    home_appliances = models.ForeignKey(
        HomeApplianceProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    kitchen = models.ForeignKey(
        KitchenProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    landscape_garden = models.ForeignKey(
        LandscapeProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    light = models.ForeignKey(
        LightProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    rugs_mat = models.ForeignKey(
        RugsMatFloorProducts, on_delete=models.CASCADE, blank=True, null=True
    )
    security_protection = models.ForeignKey(
        SecurityProtectionProducts, on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        constraints = [
            checkImageOwner(name="%(app_label)s_%(class)s_value_matches_type")
        ]

    def __str__(self):
        return self.alt

    @property
    def owner(self):
        if self.material_id is not None:
            return self.material
        if self.bathroom_id is not None:
            return self.bathroom
        if self.decorations_id is not None:
            return self.decorations
        if self.fabric_textile_id is not None:
            return self.fabric_textile
        if self.hardware_tool_id is not None:
            return self.hardware_tool
        if self.home_appliances_id is not None:
            return self.home_appliances
        if self.kitchen_id is not None:
            return self.kitchen
        if self.landscape_garden_id is not None:
            return self.landscape_garden
        if self.light_id is not None:
            return self.light
        if self.rugs_mat_id is not None:
            return self.rugs_mat
        if self.security_protection_id is not None:
            return self.security_protection
        raise AssertionError("No owner for image defined")
