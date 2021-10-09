from rest_framework import serializers
from .models import Material, ProductImage, Category


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class MaterialSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    material_type = CategorySerializer(many=True)

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
