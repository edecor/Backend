from rest_framework import serializers

from products.models import material

from .models import Room
from products.serializers import MaterialSerializer


class RoomSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, source="material_set")

    class Meta:
        model = Room
        fields = [
            "name",
            "materials",
        ]
