from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsListingOwnerOrReadOnly(BasePermission):
    '''
    Anyone can view a listing however only the poster can update/delete
    their own listing. 
    '''
    message = 'Editing listings is restricted to the poster'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # i.e. Get, Head, Options
            return True
        
        return request.user.id == obj.poster.id

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