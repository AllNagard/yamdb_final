from rest_framework import permissions


class IsAdminOrMe(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_staff or request.user.role == 'admin'
