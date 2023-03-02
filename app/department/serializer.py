from rest_framework import serializers

from .models import DepartmentModel


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentModel
        fields = "__all__"
        depth = 1

    def validate_name_en(self, value):
        if len(value) != 5:
            raise serializers.ValidationError(
                "Department name en must be 5 characters!")
        return value

    def validate_name_kh(self, value):
        if len(value) != 5:
            raise serializers.ValidationError(
                "Department name kh must be 5 characters!")
        return value
