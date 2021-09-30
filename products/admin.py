from django.contrib import admin
from .models import Category, Product, ProductImage
from django.db.models import Count
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django_json_widget.widgets import JSONEditorWidget


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class ProductImagesInline(admin.TabularInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "available", "created", "updated", "image_count"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]
    inlines = [
        ProductImagesInline,
    ]

    fields = [
        "name",
        "slug",
        "description",
        "price",
        "additional_fields",
        "categories",
        "available",
    ]

    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
        models.JSONField: {"widget": JSONEditorWidget(width="50%")},
    }
