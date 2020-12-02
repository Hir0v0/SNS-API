from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework.serializers import Serializer
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    """Serializer for non-users"""

    class Meta:
        model=models.User
        exclude=('is_active','is_staff','is_admin', 'last_login', 'first_login')
        extra_kwargs={
            'password':{'write_only':True},
            'email':{'write_only':True}
            }
    def save(self):
        """Create and return user"""
        user=models.User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        #set password
        user.set_password(self.validated_data['password'])
        #add user to DB
        user.save()

        return user