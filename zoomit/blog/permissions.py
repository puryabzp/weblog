from rest_framework.permissions import BasePermission,SAFE_METHODS


class IsPostAuthorOrReadOnly(BasePermission):
    """
       A base class from which all permission classes should inherit.
       """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user == obj.author or
            request.user.is_staff
        )

