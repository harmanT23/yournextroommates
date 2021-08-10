from typing import List
from rest_framework import generics
from roommates.models import Listing
from django.contrib.auth import get_user_model
from .serializers import ListingSerializer, UserSerializer,\
                         RegisterUserSerializer
from .permissions import IsListingOwnerOrReadOnly, IsUserOwnerOrReadOnly
from rest_framework.permissions import AllowAny,\
                                       DjangoModelPermissionsOrAnonReadOnly

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


# class UploadUserAvatar(generics.ListCreateAPIView):
#     pass

# class UploadUserGallery(generics.RetrieveDestroyAPIView):
#     pass

# class UploadListingGallery(generics.ListCreateAPIView):
#     pass
