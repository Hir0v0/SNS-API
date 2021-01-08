#from project0001api import message
from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Message, Reply
from .serializers import MessageSerializer, replySerializer
from django.shortcuts import get_object_or_404


# class MessageList(generics.ListAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

# class MessageDetail(generics.RetrieveAPIView):
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ReplyViewSet(ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = replySerializer

    def perform_create(self,serializer):
       
        comment = get_object_or_404(Message, pk=self.kwargs.get('message_pk'))
        #post = message.post

        #reply = Message.save(commit=False)
        #reply.parent = comment
        #reply.post = post
        #reply.save()
        serializer.save(author=self.request.user,post=comment,)
        #return redirect('', pk=post.pk)