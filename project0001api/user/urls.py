from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router=DefaultRouter()
#add user model basic REST-request paths
router.register('user', views.UserViewSet) 
#add login to paths
router.register('login', views.LoginViewSet, basename="Log in")


urlpatterns = [
    path(r'', include(router.urls)),
]