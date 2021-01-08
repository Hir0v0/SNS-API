from rest_framework import serializers

class FilterCommentSerializer(serializers.ListSerializer):
    """serializer which filter only parent comments"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)

class RecursiveSerializer(serializers.Serializer):
    """Serializer for comments tree"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data