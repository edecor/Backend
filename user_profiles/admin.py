from django.contrib import admin

from .models import WishItem, WishList, Customer


@admin.register(WishItem)
class WishItemAdmin(admin.ModelAdmin):
    pass


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
