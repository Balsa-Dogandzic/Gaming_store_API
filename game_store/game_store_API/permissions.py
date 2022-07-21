"""
A file for custom permissions
"""
from rest_framework import permissions
from rest_framework import status
from rest_framework.exceptions import APIException

class NotAdmin(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = {
        "message":"You don't have permissions for this action"
        }
    default_code = 'not_authenticated'


class UserIsAdmin(permissions.BasePermission):

    allowed = ("GET","POST","PUT","DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.admin:
            return True
        raise NotAdmin()

    def has_object_permission(self, request, view, obj):
        if request.user.admin and request.method in self.allowed:
            return True
        return False