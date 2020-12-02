from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Set permissions for post or comment author"""
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated