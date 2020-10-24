from rest_framework import permissions

class UserEditPermission(permissions.BasePermission):
    """Set permissions to users for actions with ther profiles"""
    def has_object_permission(self, request, view, obj):
        """Checking user privileges"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id==request.user.id