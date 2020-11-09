# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name="user"

urlpatterns = [
    path('user/', views.UserCreate.as_view()),
    path('user/<int:pk>/', views.UserProfile.as_view()),
    path('user/login', obtain_jwt_token, name="token"),
    # path('logout',views.UserLogout.as_view()),
]