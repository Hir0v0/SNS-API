from rest_framework import serializers
from .models import Post
from comment.serializers import ListCommentSerializer

class PostSerializer(serializers.ModelSerializer):
    """ Edit and display post """
    user = serializers.ReadOnlyField(source='user.username')
    comments = ListCommentSerializer(many=True, read_only=True)
    view_count = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "created_at", "user", "text", "comments", "view_count")


class ListPostSerializer(serializers.ModelSerializer):
    """ Post list"""
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ("id", "created_at", "user", "text", "comments_count")