from rest_framework import serializers
from .models import Follower
from ..user.serializers import UserByFollowerSerializer


class FollowersListSerializer(serializers.ModelSerializer):
    follower = UserByFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('follower',)

