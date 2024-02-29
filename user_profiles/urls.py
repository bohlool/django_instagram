from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FollowingViewSet, FollowersViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'following', FollowingViewSet, basename='following')
router.register(r'followers', FollowersViewSet, basename="followers")
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/profile/', include(router.urls)),
]
