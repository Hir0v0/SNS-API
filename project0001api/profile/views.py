from django.shortcuts import render
from user.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,generics
from .permissions import ProfileEditPermission
from .serializers import ProfileSerializer

class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """User profile viewset"""
    queryset = User.objects.all() 
    serializer_class=ProfileSerializer
    permission_classes=(permissions.IsAuthenticated, ProfileEditPermission)

    def get_object(self):
        return self.request.user