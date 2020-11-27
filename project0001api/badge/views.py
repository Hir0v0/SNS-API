from django.shortcuts import render
from user.models import Badge
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import BadgeSerializer
from  .permissions import IsAdminOrReadOnly

class BadgesViewSet(ModelViewSet):
    """Users badges viewset"""
    queryset = Badge.objects.all() 
    serializer_class=BadgeSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
