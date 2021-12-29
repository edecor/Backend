from django.contrib import admin
from django.db.models import fields
from .models import (
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
    ProductImage,
    Brand,
)

from ckeditor.widgets import CKEditorWidget
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


class MaterialProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "material", "product_type"]


class BathroomProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "bathroom", "product_type"]


class DecorationsProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "decorations", "product_type"]


class FabricTextileProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "fabric_textile", "product_type"]


class FurnitureProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "furniture", "product_type"]


class HardwareToolProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "hardware_tool", "product_type"]


class HomeAppliancesProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "home_appliances", "product_type"]


class KitchenProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "kitchen", "product_type"]


class LandscapeGardenProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = [
        "image",
        "alt",
        "is_description_image",
        "landscape_garden",
        "product_type",
    ]


class LightProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "light", "product_type"]


class RugsMatProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = ["image", "alt", "is_description_image", "rugs_mat", "product_type"]


class SecurityProtectionProductImageAdmin(admin.TabularInline):
    model = ProductImage
    fields = [
        "image",
        "alt",
        "is_description_image",
        "security_protection",
        "product_type",
    ]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    fields = [
        "name",
        "slug",
        "description",
        "price",
        "available",
        "uuid",
        "additional_fields",
        "place_of_origin",
        "color",
        "material_place",
        "material_category",
        "rooms",
        "thickness",
        "size",
        "shape",
        "density",
    ]
    readonly_fields = ["uuid", "slug"]

    inlines = [MaterialProductImageAdmin]

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
        models.JSONField: {"widget": JSONEditorWidget(height=300, width="50%")},
    }


@admin.register(BathroomProducts)
class BathroomProductsAdmin(admin.ModelAdmin):
    inlines = [BathroomProductImageAdmin]


@admin.register(DecorationsProducts)
class DecorationProductsAdmin(admin.ModelAdmin):
    inlines = [DecorationsProductImageAdmin]


@admin.register(FabricTextileProducts)
class FabricTextileProductsAdmin(admin.ModelAdmin):
    inlines = [DecorationsProductImageAdmin]


@admin.register(FurnitureProducts)
class FurnitureProductsAdmin(admin.ModelAdmin):
    readonly_fields = ["uuid", "slug"]
    inlines = [FurnitureProductImageAdmin]


@admin.register(HardwareToolProducts)
class HardwareToolProductsAdmin(admin.ModelAdmin):
    inlines = [HardwareToolProductImageAdmin]


@admin.register(HomeApplianceProducts)
class HomeApplianceProductsAdmin(admin.ModelAdmin):
    inlines = [HomeAppliancesProductImageAdmin]


@admin.register(KitchenProducts)
class KitchenProductsAdmin(admin.ModelAdmin):
    inlines = [KitchenProductImageAdmin]


@admin.register(LandscapeProducts)
class LandscapeProductsAdmin(admin.ModelAdmin):
    inlinse = [LandscapeGardenProductImageAdmin]


@admin.register(LightProducts)
class LightProductsAdmin(admin.ModelAdmin):
    inlines = [LightProductImageAdmin]


@admin.register(RugsMatFloorProducts)
class RugsMatFloorProductsAdmin(admin.ModelAdmin):
    inlines = [RugsMatProductImageAdmin]


@admin.register(SecurityProtectionProducts)
class SecurityProtectionProductsAdmin(admin.ModelAdmin):
    inlines = [SecurityProtectionProductImageAdmin]
