import uuid

from django.db import models
from django.conf import settings

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
from .utils import checkWishOwner


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.user.email


class WishItem(models.Model):
    class ProductWishOwner(models.TextChoices):
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

    product_type = models.CharField(
        max_length=25,
        choices=ProductWishOwner.choices,
        default=ProductWishOwner.MATERIAL,
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
            checkWishOwner(name="%(app_label)s_%(class)s_value_matches_type")
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


class WishList(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    wishes = models.ManyToManyField(WishItem)

    def __str__(self):
        return self.name
