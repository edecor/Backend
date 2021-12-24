from collections import OrderedDict

from rest_framework import serializers
from .models import Material, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )

    class Meta:
        model = ProductImage
        fields = ["id", "image", "alt", "is_description_image"]


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
