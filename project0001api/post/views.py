from django.shortcuts import render
from rest_framework import permissions, generics
from .serializers import ListPostSerializer, PostSerializer,CreateCommentSerializer
from project0001api.src.permissions import IsAuthor
from project0001api.src.views import CreateRetrieveUpdateDestroy,CreateUpdateDestroy
from .models import Post, Comment

# Create your views here.
class PostListView(generics.ListAPIView):
    """ Post feed """
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('author').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD поста
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentsView(CreateUpdateDestroy):
    """ CRUD комментариев к запси
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes_by_action = {'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()