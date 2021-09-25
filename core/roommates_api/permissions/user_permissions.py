from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOwnerOrReadOnly(BasePermission):
    '''
    Only authenticated users a can view a specific user's profile, and only 
    the original user can update/delete their own profile
    '''
    message = 'Editing a user\'s profile is restricted to the original user'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.id == obj.id
        