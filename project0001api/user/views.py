from rest_framework import permissions, status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from . import serializers,models
from .permissions import UserEditPermission
from rest_framework.permissions import AllowAny

class UserCreate(generics.CreateAPIView):
    """ Register user"""
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny,)

class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes=(permissions.IsAuthenticated, UserEditPermission)
    

@api_view(['POST'])
@permission_classes((AllowAny, ))
def login_view(request):
    """View for login, return Bearer Token"""
    serializer=serializers.UserLoginSerializer(data=request.data)
    #initilize object to be returned to view
    data={}
    #check posted data
    if serializer.is_valid():
        user=serializer.validate(request.data)
        data['responce']="Successfully logged in user"
        data['email']=user.email
        
    else:
        data=serializer.errors
    return Response(data)

