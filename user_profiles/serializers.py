from collections import OrderedDict

from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Customer, WishItem, WishList
from products.serializers import MaterialSerializer

custom_user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user_model
        fields = ["email", "date_joined"]


class WishtItemSerializerInCustomerProfileSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    # https://newbedev.com/remove-null-fields-from-django-rest-framework-response
    # todo: research properly
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )

    class Meta:
        model = WishItem
        fields = [
            "id",
            "product_type",
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


class WishtItemSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )

    class Meta:
        model = WishItem
        fields = "__all__"


class WishListSerializerInCustomerProfileSerializer(serializers.ModelSerializer):
    wishes = WishtItemSerializerInCustomerProfileSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["name", "date_modified", "wishes"]


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    wishlists = WishListSerializerInCustomerProfileSerializer(many=True)

    class Meta:
        model = Customer
        fields = ["user", "uuid", "first_name", "last_name", "wishlists"]


class CustomerProfileSerializerInWishListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ["user", "uuid", "first_name", "last_name"]


class WishListSerializer(serializers.ModelSerializer):
    customer = CustomerProfileSerializerInWishListSerializer()
    wishes = WishtItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["name", "date_modified", "customer", "wishes"]
