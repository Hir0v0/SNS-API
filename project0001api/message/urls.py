from django.urls import path

from . import views

urlpatterns = [
    #path('', views.MessageList.as_view()),
    #path('<int:pk>/', views.MessageDetail.as_view()),
    path('', views.MessageViewSet.as_view({'get':'list', 'post':'create'})),
    path('message/<int:pk>', views.MessageViewSet.as_view({'get':'retrieve', 'delete': 'destroy', 'put':'update'}),name='message'),
    path('reply/<int:message_pk>/', views.ReplyViewSet.as_view({'get':'retrieve', 'post':'create','delete': 'destroy'}), name='reply'),
]