from rest_framework import serializers
from .models import Material, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    productimage_set = ProductImageSerializer(many=True)

    class Meta:
        model = Material
        fields = [
            "uuid",
            "name",
            "slug",
            "description",
            "productimage_set",
            "price",
            "available",
            "updated",
            "additional_fields",
        ]
