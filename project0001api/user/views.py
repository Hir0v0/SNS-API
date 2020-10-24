from rest_framework import status,viewsets,filters
from .models import User 
from . import serializers,permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
    """Handling basic model functions"""
    serializer_class=serializers.UserSerializer
    queryset=User.object.all()
    authentication_classes=[TokenAuthentication,]
    permission_classes=(permissions.UserEditPermission,)
    filter_backends = (filters.SearchFilter, )
    search_fields=('username',)

class LoginViewSet(viewsets.ViewSet):
    """Handling user authentication"""
    serializer_class=AuthTokenSerializer
    def create(self, request):
        """Use ObtainAuthToken to validate and create token"""
        #check credentials
        serializer = self.serializer_class(data=request.data)
        #if matched return restframework token
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])
            return Response({'token': token.key})
        #if not matched, return error
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
