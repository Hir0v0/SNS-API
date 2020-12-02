from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BadgesViewSet
app_name = "badges"

router = DefaultRouter()
router.register(r'', BadgesViewSet, basename='badge')
urlpatterns = router.urls