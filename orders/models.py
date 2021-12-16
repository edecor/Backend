import functools
import operator

from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.constraints import CheckConstraint

from products.models import (
    Material,
    BathroomProducts,
    DecorationsProducts,
    FabricTextileProducts,
    FurnitureProducts,
    HardwareToolProducts,
    HomeApplianceProducts,
    KitchenProducts,
    LandscapeProducts,
    LightProducts,
    RugsMatFloorProducts,
    SecurityProtectionProducts,
)


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    billing_status = models.BooleanField(default=False)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return str(self.order_date)


def checkOrderOwner(name):
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


class OrderItem(models.Model):
    class ProductOrderOwner(models.TextChoices):
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

    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    product_type = models.CharField(
        max_length=25,
        choices=ProductOrderOwner.choices,
        default=ProductOrderOwner.MATERIAL,
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

    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveBigIntegerField(default=1)

    class Meta:
        constraints = [
            checkOrderOwner(name="%(app_label)s_%(class)s_value_matches_type")
        ]

    def __str__(self):
        return str(self.id)

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
