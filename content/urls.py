from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, StoryViewSet, MediaViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'media', MediaViewSet)
router.register(r'stories', StoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
