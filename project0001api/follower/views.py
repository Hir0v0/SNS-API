from rest_framework import generics, permissions, views, response
from .models import Follower
from .serializers import FollowersListSerializer
from ..user.models import User


class ListOfFollowersView(generics.ListAPIView):
    """List of follower view"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowersListSerializer

    def get_queryset(self):
        return Follower.objects.filter(user=self.request.user)


class AddFollowerView(views.APIView):
    """Follow user view"""
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        Follower.objects.create(follower=self.request.user)
        return response.Response(status=201)

    def delete(self, request, pk):
        try:
            record = Follower.objects.get(subscriber=request.user, user_id=pk)
        except Follower.DoesNotExist:
            return response.Response(status=404)
        record.delete()
        return response.Response(status=204)
