from django.urls import path
from . import views
app_name="comment"

urlpatterns = [
    path('comment', views.PostCommentsView.as_view({'post': 'create'})),
    path('comment/<int:pk>', views.PostCommentsView.as_view({'get':'retrieve',
                                                        'put': 'update', 
                                                        'delete': 'destroy'})),
]