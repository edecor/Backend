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


def return_product_image_directory(instance, filename):

    # the following is basically just komedi code

    if instance.product_type == "material":
        product_instance = instance.material
    elif instance.product_type == "bathroom":
        product_instance = instance.bathroom
    elif instance.product_type == "decorations":
        product_instance = instance.decorations
    elif instance.product_type == "furniture":
        product_instance = instance.furniture
    elif instance.product_type == "fabric_textile":
        product_instance = instance.fabric_textile
    elif instance.product_type == "hardware_tool":
        product_instance = instance.hardware_tool
    elif instance.product_type == "home_appliances":
        product_instance = instance.home_appliances
    elif instance.product_type == "kitchen":
        product_instance = instance.kitchen
    elif instance.product_type == "landscape_garden":
        product_instance = instance.landscape_garden
    elif instance.product_type == "light":
        product_instance = instance.light
    elif instance.product_type == "rugs_mat":
        product_instance = instance.rugs_mat
    elif instance.product_type == "security_protection":
        product_instance = instance.security_protection
    else:
        assert instance.product_type is not None

    if instance.is_description_image:
        return f"products/{product_instance.slug}/description/{filename}"
    return f"products/{product_instance.slug}/main/{filename}"


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
    class ProductImageOwner(models.TextChoices):
        MATERIAL = "material"
        BATHROOM = "bathroom"
        DECORATIONS = "decorations"
        FURNITURE = "furniture"
        FABRIC_TEX = "fabric_textile"
        HARDWARE_TOOL = "hardware_tool"
        HOME_APPLIANCES = "home_appliances"
        KITCHEN = "kitchen"
        LANDSCAPE = "landscape_garden"
        LIGHT = "light"
        RUGS_MAT = "rugs_mat"
        SEC_PROT = "security_protection"

    image = VersatileImageField(
        upload_to=return_product_image_directory,
        max_length=600,
    )
    alt = models.CharField(max_length=128)

    is_description_image = models.BooleanField(default=False)

    product_type = models.CharField(
        max_length=25,
        choices=ProductImageOwner.choices,
        default=ProductImageOwner.MATERIAL,
    )

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
