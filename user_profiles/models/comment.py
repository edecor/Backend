from django.db import models
from versatileimagefield.fields import VersatileImageField

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

from user_profiles.models import Customer
from user_profiles.utils import checkCommentOwner


class Comment(models.Model):
    class CommentOwnerProduct(models.TextChoices):
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
        choices=CommentOwnerProduct.choices,
        default=CommentOwnerProduct.MATERIAL,
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    comment_text = models.TextField()

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
            checkCommentOwner(name="%(app_label)s_%(class)s_value_matches_type")
        ]

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
        raise AssertionError("No owner for comment defined")

    def __str__(self):
        return str(self.id)


def return_product_image_directory(instance, filename):
    comment_instance = instance.comment
    if isinstance(comment_instance.material, Material):
        product_instance = comment_instance.material
    if isinstance(comment_instance.bathroom, BathroomProducts):
        product_instance = comment_instance.bathroom
    if isinstance(comment_instance.decoration, DecorationsProducts):
        product_instance = comment_instance.decoration
    if isinstance(comment_instance.furniture, FurnitureProducts):
        product_instance = comment_instance.furniture
    if isinstance(comment_instance.fabric_textile, FabricTextileProducts):
        product_instance = comment_instance.fabric_textile
    if isinstance(comment_instance.hardware_tool, HardwareToolProducts):
        product_instance = comment_instance.hardware_tool
    if isinstance(comment_instance.home_appliances, HomeApplianceProducts):
        product_instance = comment_instance.home_appliances
    if isinstance(comment_instance.kitchen, KitchenProducts):
        product_instance = comment_instance.kitchen
    if isinstance(comment_instance.landscape_garden, LandscapeProducts):
        product_instance = comment_instance.landscape_garden
    if isinstance(comment_instance.lights, LightProducts):
        product_instance = comment_instance.lights
    if isinstance(comment_instance.rugs_mat, RugsMatFloorProducts):
        product_instance = comment_instance.rugs_mat
    if isinstance(comment_instance.security_protection, SecurityProtectionProducts):
        product_instance = comment_instance.security_protection

    return f"products/{product_instance.slug}/comments/{filename}"


class CommentImage(models.Model):
    src = VersatileImageField(upload_to=return_product_image_directory)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    alt = models.CharField(max_length=50)

    def __str__(self):
        return self.alt
