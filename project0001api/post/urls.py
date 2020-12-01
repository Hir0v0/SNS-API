from django.urls import path
from . import views
app_name="post"

urlpatterns = [
    path('', views.PostView.as_view({'post': 'create'})),
    path('<int:pk>', views.PostView.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'destroy'
    })),
    path('user/<int:pk>', views.PostListView.as_view()),
]