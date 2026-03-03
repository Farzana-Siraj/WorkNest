from rest_framework import serializers

from .models import Form


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["id", "name", "created_at"]
        read_only_fields = ["id", "created_at"]
