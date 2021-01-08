from django.db.models import fields
from rest_framework import serializers
from . import models

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source = 'user.username')
    likes =  serializers.IntegerField(read_only=True)
    flag = serializers.BooleanField(read_only=True)

    class Meta:
        fields = ('__all__')
        model = models.Message

class replySerializer(serializers.ModelSerializer):
    likes =  serializers.IntegerField(read_only=True)
    post = serializers.IntegerField(read_only=True)
    author = serializers.CharField(read_only=True)
    parent = serializers.IntegerField(read_only=True)
    
    class Meta:
        fields = ('__all__')
        model = models.Reply