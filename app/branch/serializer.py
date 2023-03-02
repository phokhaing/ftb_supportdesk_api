from rest_framework import serializers

from .models import BranchModel


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchModel
        fields = "__all__"
        depth = 1

    def validate_code(self, value):
        if len(value) != 9:
            raise serializers.ValidationError("Branch code must 9 characters!")
        return value

    # validate all fields
    def validate(self, data):
        if (len(data.get('name_en')) < 5):
            raise serializers.ValidationError(
                "Branch name en must be 9 characters!")

        return data
