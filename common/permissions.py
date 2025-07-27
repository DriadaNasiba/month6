from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAnonymousReadOnly(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_authenticated and request.method in SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Разрешить только владельцу
        return obj.owner == request.user


class IsModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.is_staff and
            request.method != 'POST'
        )

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
