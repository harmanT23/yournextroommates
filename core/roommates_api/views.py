from roommates.models import Listing
from django.contrib.auth import get_user_model

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ListingSerializer, UserSerializer,\
                         RegisterUserSerializer
from .permissions import IsListingOwnerOrReadOnly, IsUserOwnerOrReadOnly
from rest_framework.permissions import AllowAny,\
                                       DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.tokens import RefreshToken



User = get_user_model()

class ListingList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Listing.listingobjects.all().order_by('id')
    serializer_class = ListingSerializer
    

class ListingDetail(generics.RetrieveUpdateDestroyAPIView, 
                    IsListingOwnerOrReadOnly):
    permission_classes = [IsListingOwnerOrReadOnly]
    queryset = Listing.listingobjects.all().order_by('id')
    serializer_class = ListingSerializer


class UserCreate(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all().order_by('id')
    serializer_class = RegisterUserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView, IsUserOwnerOrReadOnly):
    permission_classes = [IsUserOwnerOrReadOnly]
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

class BlackListTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
            try:
                refresh_token = request.data['refresh_token']
                token = RefreshToken(refresh_token)
                token.blacklist()
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# class UploadUserAvatar(generics.ListCreateAPIView):
#     pass

# class UploadUserGallery(generics.RetrieveDestroyAPIView):
#     pass

# class UploadListingGallery(generics.ListCreateAPIView):
#     pass
