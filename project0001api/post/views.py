
from rest_framework import permissions, generics
from .serializers import ListPostSerializer, PostSerializer
from comment.serializers import CreateCommentSerializer
from project0001api.src.permissions import IsAuthor
from project0001api.src.views import CreateRetrieveUpdateDestroy,CreateUpdateDestroy
from .models import Post

# Create your views here.
class PostListView(generics.ListAPIView):
    """ user's wall """
    serializer_class = ListPostSerializer

    def get_queryset(self):
        return Post.objects.filter(
            user_id=self.kwargs.get('pk')).select_related('user').prefetch_related('comments')


class PostView(CreateRetrieveUpdateDestroy):
    """ CRUD for post
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    queryset = Post.objects.all().select_related('user').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes_by_action = {'get': [permissions.AllowAny],
                                    'update': [IsAuthor],
                                    'destroy': [IsAuthor]}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

