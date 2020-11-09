from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """Serializer for users"""
    class Meta:
        model=models.User
        fields=('id','email','password','username')
        extra_kwargs={'password':{'write_only':True}}

    def create(self, validated_data):
        """Create and return user"""
        user=models.User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        #set password
        user.set_password(validated_data['username'])
        #add user to DB
        user.save()

        return user
