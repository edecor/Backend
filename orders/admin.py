from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInlineAdmin(admin.StackedInline):
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInlineAdmin]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass
