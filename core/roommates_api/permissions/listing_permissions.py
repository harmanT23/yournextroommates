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
        