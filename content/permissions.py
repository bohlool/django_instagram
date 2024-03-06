from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsOwnerOrSuperuserOrReadonly(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if request.method in SAFE_METHODS:
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own content
        if obj.user == request.user:
            return True

        return False


class IsMediaOwnerOrSuperuserOrReadonly(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if request.method in SAFE_METHODS:
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own content
        if obj.post.user == request.user:
            return True

        return False
