from django.contrib import admin
from .models import (
    Category,
    Material,
    ProductImage,
    Brand,
    Supplier,
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
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.contenttypes.admin import GenericTabularInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class ProductImagesInline(GenericTabularInline):
    model = ProductImage


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "available", "created", "updated", "image_count"]
    list_filter = ["available", "created", "updated", "material_type"]
    list_editable = ["price", "available"]
    inlines = [
        ProductImagesInline,
    ]

    readonly_fields = ("uuid", "slug")
    # fields = [
    #     "name",
    #     "slug",
    #     "description",
    #     "price",
    #     "additional_fields",
    #     "categories",
    #     "available",
    #     "uuid",
    # ]

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
        models.JSONField: {"widget": JSONEditorWidget(height=300, width="50%")},
    }


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(BathroomProducts)
class BathroomProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(DecorationsProducts)
class DecorationProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(FabricTextileProducts)
class FabricTextileProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(FurnitureProducts)
class FurnitureProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(HardwareToolProducts)
class HardwareToolProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(HomeApplianceProducts)
class HomeApplianceProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(KitchenProducts)
class KitchenProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(LandscapeProducts)
class LandscapeProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(LightProducts)
class LightProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(RugsMatFloorProducts)
class RugsMatFloorProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(SecurityProtectionProducts)
class SecurityProtectionProductsAdmin(admin.ModelAdmin):
    pass
