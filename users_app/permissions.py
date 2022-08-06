from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Permissions user update own profile """

    def has_object_permission(self, request, view, obj):
        """ Verify if user is try update own profile """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id