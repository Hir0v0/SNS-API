from rest_framework import serializers

from project0001api.src.serializers import RecursiveSerializer, FilterCommentSerializer
from .models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """ Add comment to postserializer """
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")

class CommentListSerializer(serializers.ModelSerializer):
    """ comment list"""
 #   user = serializers.ReadOnlyField(source='user.username')
#
 #   class Meta:
  #      model = Comment
   #     fields = ("id", "created_at", "user", "text")
#

class ListCommentSerializer(serializers.ModelSerializer):
    """ Comments list serializer """
    text = serializers.SerializerMethodField()
    children = RecursiveSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_at", "is_deleted", "children")
