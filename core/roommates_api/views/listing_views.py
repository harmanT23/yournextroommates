from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from roommates.models import Listing
from ..serializers import (
    CreateListingSerializer,
    ListingSerializer,
)
from ..filters import ListingFilter
from ..permissions import IsListingOwnerOrReadOnly


class ListingListView(generics.ListCreateAPIView):
    """
    Listing List Endpoint
    - GET: Retrieve a list of listings
    - POST: Create a brand new listing
    """

    queryset = Listing.objects.all()

    serializers = {
        'POST': CreateListingSerializer,
        'default': ListingSerializer,
    }
    permission_classes = [IsAuthenticatedOrReadOnly,]

    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter
    ]
                       
    filterset_class = ListingFilter
    search_fields = ['city']
    ordering_fields = [
        'rent_per_month', 
        'length_of_lease', 
        'earliest_move_in_date'
    ]    

    def get_serializer_class(self):
        if hasattr(self, 'request') and hasattr(self.request, 'method'):
            return self.serializers.get(
                self.request.method, 
                self.serializers['default']
            )
        else:
            return ListingSerializer



class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Listing Detail Endpoint
    - GET: Get a listing by slug
    - PUT or PATCH: Update a listing by slug
    - DELETE: Delete a listing by slug
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticatedOrReadOnly,]
        else:
            self.permission_classes = [IsListingOwnerOrReadOnly,]
        return super(ListingDetailView, self).get_permissions()

    def get_object(self, queryset=None, **kwargs):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Listing, slug=slug_)
    