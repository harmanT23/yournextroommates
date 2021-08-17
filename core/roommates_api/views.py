from roommates.models import Listing
from .serializers import CreateListingSerializer, ListingSerializer,\
                         UserSerializer,\
                         RegisterUserSerializer
from .permissions import IsListingOwnerOrReadOnly, IsUserOwnerOrReadOnly
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated,\
     IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


# Endpoint for displaying all listings and creating new ones
class ListingViewset(viewsets.ModelViewSet):
    serializers = {
        'create': CreateListingSerializer,
        'default': ListingSerializer,
    }
        
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
    
class UserViewset(viewsets.ModelViewSet):
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
        elif self.action == 'list':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [IsUserOwnerOrReadOnly]
        return super(UserViewset, self).get_permissions()
    
    def get_queryset(self):
        return User.objects.all().order_by('id')
    
    def get_object(self, queryset=None, **kwargs):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk_)
    
    # Disable being able to list a set of users
    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
