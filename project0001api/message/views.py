from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message


class MessageView(APIView):
    """API view for Message model"""
    def get(self, request):
        """Get message with id"""
        return Response({"message": "hello"})