from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their profile only"""

    def has_object_permission(self, request, view, obj):
        """Check user trying to edit profile"""
        """if request method is SAFE_METHODS (get) allow"""
        if request.method in permissions.SAFE_METHODS:
            return True

        """if not get request, if obj.id === return user id"""
        return obj.id == request.user.id
