from rest_framework import permissions


class AuthorStaffOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in ('GET',)
            or (request.user == obj.author)
            or request.user.is_staff
        )


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in ('GET', )
            or request.user.is_authenticated
            and request.user.is_admin
        )


class OwnerUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
