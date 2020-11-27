from rest_framework import serializers
from user.models import Badge

class BadgeSerializer(serializers.ModelSerializer):
    """Serializer for badges"""
    class Meta:
        model=Badge
        fields=('__all__')
