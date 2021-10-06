from django.contrib import admin
from .models import Category, Material, ProductImage, Brand, Supplier
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
