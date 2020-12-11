from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Set permissions foradmin for actions with editing"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_admin
