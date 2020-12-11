from django.shortcuts import render
from project0001api.src.permissions import IsAuthor
from rest_framework import permissions, generics
from project0001api.src.views import CreateRetrieveUpdateDestroy
from .models import Comment
from .serializers import CreateCommentSerializer


class PostCommentsView(CreateRetrieveUpdateDestroy):
    """ CRUD for comment to post"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor],
                                    'retrieve': [permissions.AllowAny]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()
