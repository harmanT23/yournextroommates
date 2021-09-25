from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserImageOwnerOrReadOnly(BasePermission):
    '''
    Only authenticated users can view another user's image gallery but only
    the user themselves can update/delete their own images.
    '''

    message = 'Editing a user\'s images is restricted to the original user'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.id == obj.user.id
        