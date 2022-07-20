"""
A file for custom permissions
"""
from rest_framework import permissions


class UserIsAdmin(permissions.BasePermission):

    allowed = ("GET","POST","PUT","DELETE")

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.admin:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.admin and request.method in self.allowed:
            return True

        return False