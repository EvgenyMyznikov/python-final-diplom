from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    custom permission
    """
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author
        return obj.author == request.user

# Allow read-only for all requests but for any write requests,
# such as edit or delete, the author must be the same as the current logged-in user