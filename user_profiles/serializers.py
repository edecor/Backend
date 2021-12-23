from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Customer

custom_user_model = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = custom_user_model
        fields = [
            "email",
            "date_joined",
        ]


class CustomerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ["user", "uuid", "first_name", "last_name"]
