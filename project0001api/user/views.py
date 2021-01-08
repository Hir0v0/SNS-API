from rest_framework import permissions, status, generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import User
from .serializers import UserSerializer
from . import serializers
from .permissions import UserEditPermission


class UserViewSet(ModelViewSet):
    """Public user viewset"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login_view(request):
    """endpoint for login, return Bearer Token"""
    serializer = serializers.UserLoginSerializer(data=request.data)
    # initilize object to be returned to view
    data = {}
    # check posted data
    if serializer.is_valid():
        user = serializer.validate(request.data)
        data['responce'] = "Successfully logged in user"
        data['email'] = user.email

    else:
        data = serializer.errors
    return Response(data)
