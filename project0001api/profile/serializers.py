from rest_framework import serializers
from user.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.serializers import Serializer
from rest_framework.response import Response

class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for users"""
    avatar=serializers.ImageField(read_only=True)
    class Meta:
        model=User
        exclude=('is_active','is_staff','is_admin', 'last_login', 'first_login')
        extra_kwargs={
            'password':{'write_only':True}
            }
