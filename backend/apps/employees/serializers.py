from rest_framework import serializers

from .models import EmployeeData


class EmployeeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeData
        fields = ["id", "form", "data", "created_at"]
        read_only_fields = ["id", "created_at"]
