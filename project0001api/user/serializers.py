from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    """Serializer for users"""
    class Meta:
        model=models.User
        exclude=('is_active','is_staff','is_admin', 'password', 'last_login', 'first_login')
        extra_kwargs={
            'password':{'write_only':True}
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
