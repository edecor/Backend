from rest_framework import serializers
from .models import Material, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Material
        fields = [
            "uuid",
            "name",
            "slug",
            "images",
            "material_type",
            "description",
            "price",
            "available",
            "updated",
            "additional_fields",
        ]
