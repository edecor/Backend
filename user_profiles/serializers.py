from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Customer, WishItem, WishList

custom_user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user_model
        fields = ["email", "date_joined"]


class WishtItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishItem
        fields = "__all__"


class WishListSerializerInCustomerProfileSerializer(serializers.ModelSerializer):
    wishes = WishtItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["name", "date_modified", "wishes"]


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    wishlists = WishListSerializerInCustomerProfileSerializer(many=True)

    class Meta:
        model = Customer
        fields = ["user", "uuid", "first_name", "last_name", "wishlists"]


class WishListSerializer(serializers.ModelSerializer):
    customer = CustomerProfileSerializer()
    wishes = WishtItemSerializer(many=True)

    class Meta:
        model = WishList
        fields = ["name", "date_modified", "customer", "wishes"]
