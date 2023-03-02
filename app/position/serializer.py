from rest_framework import serializers
from .models import PositionModel


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionModel
        fields = "__all__"
        depth = 1

    def validate_name_en(self, value):
        if len(value) != 5:
            raise serializers.ValidationError(
                "Position name en must be 5 characters!")
        return value

    def validate_name_kh(self, value):
        if len(value) != 5:
            raise serializers.ValidationError(
                "Position name kh must be 5 characters!")
        return value
