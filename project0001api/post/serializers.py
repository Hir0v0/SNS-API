from rest_framework import serializers

from comment.serializers import RecursiveCommentSerializer, FilterCommentListSerializer
from .models import Post, Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    """ Add comment to postserializer    """
    class Meta:
        model = Comment
        fields = ("post", "text", "parent")


class ListCommentSerializer(serializers.ModelSerializer):
    """ Comments list serializer """
    text = serializers.SerializerMethodField()
    children = RecursiveCommentSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.username')

    def get_text(self, obj):
        if obj.is_deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ("id", "post", "user", "text", "created_at", "is_deleted", "children")


class PostSerializer(serializers.ModelSerializer):
    """ Edit and display post """
    user = serializers.ReadOnlyField(source='user.username')
    comment = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "created_at", "user", "text", "comment", "view_count")


class ListPostSerializer(serializers.ModelSerializer):
    """ Post list"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "created_at", "user", "text", "comments_count")