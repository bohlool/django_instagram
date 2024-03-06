from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsOwnerOrSuperuserOrReadonly(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if request.method in SAFE_METHODS:
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own profiles
        if obj.user == request.user:
            return True

        return False


class IsFollowingOrSuperuser(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if request.method in SAFE_METHODS:
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own followings
        if obj.follower == request.user:
            return True

        return False


class IsOwnerOrSuperuserOrPublicProfileOrFollowingReadonly(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if (request.method in SAFE_METHODS) and (obj.is_public or obj.user in request.user.profile.get_following()):
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own followings
        if obj.user == request.user:
            return True

        return False


class IsFollowerOrSuperuser(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Allow GET requests
        if request.method in SAFE_METHODS:
            return True

        # Allow superusers to perform any action
        if request.user.is_superuser:
            return True

        # Allow users to perform actions on their own followers
        if obj.followed == request.user:
            return True

        return False
