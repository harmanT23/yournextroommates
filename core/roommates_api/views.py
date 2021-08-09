from typing import List
from rest_framework import generics
from roommates.models import Listing
from django.contrib.auth import get_user_model
from .serializers import ListingSerializer, UserSerializer

User = get_user_model()


class ListingList(generics.ListCreateAPIView):
    queryset = Listing.listingobjects.all().order_by('id')
    serializer_class = ListingSerializer
    

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.listingobjects.all().order_by('id')
    serializer_class = ListingSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


# class UploadUserAvatar(generics.ListCreateAPIView):
#     pass

# class UploadUserGallery(generics.RetrieveDestroyAPIView):
#     pass

# class UploadListingGallery(generics.ListCreateAPIView):
#     pass
