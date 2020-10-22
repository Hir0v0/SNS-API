from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    """Serialize users usernames"""
    username=serializers.CharField(max_length=20)
