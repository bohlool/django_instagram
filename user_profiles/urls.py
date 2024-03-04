from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FollowingViewSet, FollowersViewSet, ProfileViewSet, RegisterViewSet, ChangePasswordViewSet, \
    ChangeAccountViewSet

router = DefaultRouter()
router.register(r'following', FollowingViewSet, basename='following')
router.register(r'followers', FollowersViewSet, basename="followers")
router.register(r'profiles', ProfileViewSet)
router.register(r'register', RegisterViewSet, basename="register")
router.register(r'change-pass', ChangePasswordViewSet, basename="change-pass")
router.register(r'change-account', ChangeAccountViewSet, basename="change-account")

urlpatterns = [
    path('api/profile/', include(router.urls)),
]
