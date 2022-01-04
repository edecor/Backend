from django.contrib import admin

from .models import WishItem, WishList, Customer, Comment, CommentImage


@admin.register(CommentImage)
class CommentImageAdmin(admin.ModelAdmin):
    pass


class CommentImageInlineAdmin(admin.TabularInline):
    model = CommentImage


@admin.register(WishItem)
class WishItemAdmin(admin.ModelAdmin):
    pass


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ["user", "first_name", "last_name", "uuid"]
    readonly_fields = ["uuid"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentImageInlineAdmin]


class MaterialCommentAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "material", "product_type"]


class BathroomProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "bathroom", "product_type"]


class DecorationsProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "decorations", "product_type"]


class FabricTextileProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "fabric_textile", "product_type"]


class FurnitureProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "furniture", "product_type"]


class HardwareToolProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "hardware_tool", "product_type"]


class HomeAppliancesProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "home_appliances", "product_type"]


class KitchenProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "kitchen", "product_type"]


class LandscapeGardenProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "landscape_garden", "product_type"]


class LightProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "light", "product_type"]


class RugsMatProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "rugs_mat", "product_type"]


class SecurityProtectionProductImageAdmin(admin.TabularInline):
    model = Comment
    fields = ["customer", "security_protection", "product_type"]
