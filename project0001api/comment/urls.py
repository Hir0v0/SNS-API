from django.urls import path
from . import views

app_name = "comment"

urlpatterns = [
    path('', views.PostCommentsView.as_view({'post': 'create'})),
    path('<int:pk>', views.PostCommentsView.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'})),
]
