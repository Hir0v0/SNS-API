"""project0001api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework import permissions
from . import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Project 0001 API",
      default_version='v1',
      description="SNS API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/', include('user.urls')),
    path('api/message/', include('message.urls')),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
=======
    path('api/v1/user/', include('user.urls')),
    path('api/v1/message/', include('message.urls')),
    path('api/v1/profile/', include('profile.urls')),
    path('api/v1/badge/', include('badge.urls')),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/comment/', include('comment.urls')),
    path('api/v1/emotion/', include('emotion.urls')),
    path('api/v1/follower/', include('follower.urls')),
    path('api/v1/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
>>>>>>> 1028fb4f4ec46e5db744bb2965e732dae2e5d301
]

if settings.DEBUG:
    """Debug server media"""
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)