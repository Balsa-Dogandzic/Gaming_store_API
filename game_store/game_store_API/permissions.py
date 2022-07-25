"""
A file for custom permissions
"""
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from rest_framework import status
from rest_framework.exceptions import APIException

class NotAdmin(APIException):
    """Custom exeption for permissions"""
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {
        "message":"You don't have permissions for this action"
        }
    default_code = 'not_authenticated'


class UserIsAdmin(permissions.BasePermission):
    """Custom admin permission class"""
    allowed = ("GET","PUT","DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.admin and request.method in self.allowed:
            return True
        raise NotAdmin()

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.admin:
            return True
        return False


class AdminUserOrReadOnly(permissions.BasePermission):
    """Custom admin or read only permission class"""
    allowed = ("GET","POST")
    def has_permission(self, request, view):
        is_admin = request.user.is_authenticated and request.user.admin
        if (is_admin and request.method in self.allowed) or request.method in SAFE_METHODS:
            return True
        raise NotAdmin()
