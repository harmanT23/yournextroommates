from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from roommates.models import Listing
from .serializers import CreateListingSerializer,\
                         ListingSerializer,\
                         UserSerializer,\
                         RegisterUserSerializer
from .permissions import IsListingOwnerOrReadOnly, IsUserOwnerOrReadOnly
from .filters import ListingFilter


User = get_user_model()


# Endpoint for displaying all listings and creating new ones
class ListingViewset(viewsets.ModelViewSet):
    '''
       Defines an endpoint for listing, viewing, retrieving, updating and
       destroying listings 
    '''
    serializers = {
        'create': CreateListingSerializer,
        'default': ListingSerializer,
    }

    filter_backends = [DjangoFilterBackend, 
                       filters.SearchFilter, 
                       filters.OrderingFilter]
                       
    filterset_class = ListingFilter
    search_fields = ['city']
    ordering_fields = ['rent_per_month', 
                       'length_of_lease', 
                       'earliest_move_in_date']
        
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        '''
        Instantiate and returns a permission for the HTTP method invoked
        '''
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            self.permission_classes = [IsListingOwnerOrReadOnly]
        return  super(ListingViewset, self).get_permissions()
        
    def get_queryset(self):
        return Listing.objects.all().order_by('id')

    def get_object(self, queryset=None, **kwargs):
        title_ = self.kwargs.get('pk')
        return get_object_or_404(Listing, slug=title_)
    
class UserViewset(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):

    serializers = {
        'create': RegisterUserSerializer,
        'default': UserSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        '''
        Instantiate and returns a permission corresponding to the HTTP method
        '''
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsUserOwnerOrReadOnly]
        return super(UserViewset, self).get_permissions()
    
    def get_queryset(self):
        return User.objects.all().order_by('id').filter(id=self.id)
    
    def get_object(self, queryset=None, **kwargs):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk_)
    
class BlackListTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# class UploadUserAvatar(generics.ListCreateAPIView):
#     pass

# class UploadUserGallery(generics.RetrieveDestroyAPIView):
#     pass

# class UploadListingGallery(generics.ListCreateAPIView):
#     pass
