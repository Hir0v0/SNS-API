# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_jwt.views import obtain_jwt_token
app_name="user"

urlpatterns = [
<<<<<<< HEAD
    path('user/', views.UserCreate.as_view()),
    path('user/<int:pk>/', views.UserProfile.as_view()),
    path('user/login', obtain_jwt_token, name="token"),
=======
    path('<int:pk>', views.UserViewSet.as_view({'get':'retrieve'})),
    path('', views.UserViewSet.as_view({'get':'list','post':'create'})),
    path('login', obtain_jwt_token, name="token"),
    #path('/register', obtain_jwt_token, name="token"),
>>>>>>> 1028fb4f4ec46e5db744bb2965e732dae2e5d301
]