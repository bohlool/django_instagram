from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'follows', FollowViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/profile/', include(router.urls)),
]
