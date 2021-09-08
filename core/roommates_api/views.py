from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, generics, filters
from rest_framework.exceptions import APIException, NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .filters import ListingFilter
from .permissions import IsListingOwnerOrReadOnly, IsUserOwnerOrReadOnly  
from .serializers import (
    CreateListingSerializer,
    ListingSerializer,
    RegisterUserSerializer,
    UserSerializer,
    GallerySerializer,
    GalleryDetailSerializer,
    GalleryImageSerializer,
    GalleryImageUploadSerializer
)
from roommates.models import Listing, Gallery, GalleryImage


User = get_user_model()


# Endpoint for displaying all listings and creating new ones
class ListingView(viewsets.ModelViewSet):
    '''
    Defines an endpoint for listing, viewing, retrieving, updating and
    destroying listings 
    '''
    serializers = {
        'create': CreateListingSerializer,
        'default': ListingSerializer,
    }

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
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            self.permission_classes = [IsListingOwnerOrReadOnly]
        return  super(ListingView, self).get_permissions()
        
    def get_queryset(self):
        return Listing.objects.all().order_by('id')

    def get_object(self, queryset=None, **kwargs):
        slug_ = self.kwargs.get('pk')
        return get_object_or_404(Listing, slug=slug_)

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
    
    def get_object(self, queryset=None, **kwargs):
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Listing, slug=slug_)

class ListingDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Listing Detail Endpoint
    - GET: Get a listing by slug
    - PUT/PATCH: Update a listing by slug
    - DELETE: Delete a listing
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
    
class UserCreateView(generics.CreateAPIView):
    """
    User Create Endpoint
    - POST: Registers a new user
    """
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny,]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Detail Endpoint
    - GET: Get a user by id
    - PUT/PATCH: Update a user by id
    - DELETE: Delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrReadOnly,]

class GalleryCreateView(generics.CreateAPIView):
    """
    Gallery Create Endpoint
    - POST: Creates a new gallery for a user or listing
    """
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated,]

class GalleryDetailView(APIView):
    """
    Gallery Detail Endpoint
    - GET: Returns all of the images for the gallery
    - POST: Upload one or more images to the gallery
    - DELETE: Delete the gallery and all its images
    """

    permission_classes = [IsAuthenticated,]

    def get(self, request, gallery_id, format=None):
        """
        Return all images within the gallery
        """
        gallery = self.get_gallery(gallery_id)
        serializer = GalleryDetailSerializer(gallery)
        return Response(serializer.data)
    
    def post(self, request, gallery_id, format=None):
        """
        Upload one or more images to the gallery
        """
        gallery = self.get_gallery(gallery_id)

        imgs_upload_status = {
            'uploaded': [],
            'errors': []
        }

        if not request.FILES:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for key, file in request.FILES.items():
                print(request.FILES[key])
                
                data = {
                    'gallery': gallery.pk,
                    'image': file
                }
                serializer = GalleryImageUploadSerializer(data=data)

                if serializer.is_valid():
                    output = serializer.save()
                    imgs_upload_status['uploaded'].append({
                        'url': output.image.url,
                    })
            
            else:
                imgs_upload_status['errors'].append({
                    'filename': file.name,
                    'error': serializer.errors
                })
        
            return Response(imgs_upload_status, status=status.HTTP_200_OK)

        except Exception as e:
            raise APIException

    def delete(self, request, gallery_id, format=None):
        """
        Delete gallery and all the images within it
        """
        gallery = self.get_gallery(gallery_id)
        gallery.delete()
        return Response(None, status=status.HTTP_200_OK)
        
    def get_gallery(self, gallery_id):
        """
        Get specified gallery instance if it exists 
        """
        gallery = Gallery.objects.filter(
            uuid=gallery_id
        ).first()

        if not gallery:
            raise NotFound("Gallery does not exist.")

        return gallery


class ImageDetailView(APIView):
    """
    Image Detail Endpoint
    GET: Get a specific image within a specified gallery by uuid
    DELETE: Delete a specific image within a specified gallery by uuid
    """
    
    permission_classes = [IsAuthenticated,]

    def get(self, request, gallery_id, image_id, format=None):
        """
        Return specified image within the gallery
        """
        gallery_image = self.get_image(gallery_id, image_id)

        data = {
            'image_url': gallery_image.image.url,
            'image_name': gallery_image.image_name
        }

        serializer = GalleryImageSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.initial_data)
    
    def delete(self, request, gallery_id, image_id, format=None):
        """
        Delete specified image instance
        """
        gallery_image = self.get_image(gallery_id, image_id)

        gallery_image.delete()
        return Response(None, status=status.HTTP_200_OK)


    def get_image(self, gallery_id, image_id):
        """
        Get specified image instance if it exists 
        """
        gallery = Gallery.objects.filter(uuid=gallery_id).first()

        if not gallery:
            raise NotFound("Gallery does not exist")

        image = GalleryImage.objects.filter(
            gallery__id=gallery.id
        ).filter(
            image_name=image_id
        ).first()

        if not image:
            raise NotFound("Image does not exist")

        return image


class BlackListTokenView(APIView):
    """
    Used to blacklist refresh tokens after a user logs out.
    """
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
