from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import User
from . import serializers

class UserView(APIView):
    """API view for User model"""

    serializer_class=serializers.UserSerializer

    def get(self, request):
        """Get user with id"""
        return Response({"users": "hello"})

    def post(self, request):
        """Create new user"""
        serializer=serializers.UserSerializer(data=request.data)
        #checking if recived values are valid
        if serializer.is_valid():
            username=serializer.data.get('username')
            message="User {0} successfully added to DB".format(username)
            return Response({
                'message':message
                })
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk=None):
        """Partialy update object"""
        return Response({
            "message":"patch method"
        })

    def delete(self, request, pk=None):
        """Delete user"""
        return Response({
            "message":"delete method"
        })