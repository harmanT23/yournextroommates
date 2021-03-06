
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model

from ..permissions import IsUserOwnerOrReadOnly
from ..serializers import (
    RegisterUserSerializer,
    UserSerializer,
)

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """
    User Create Endpoint
    - POST: Registers a new user
    """
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny,]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Detail Endpoint
    - GET: Get a user by id
    - PUT/PATCH: Update a user by id
    - DELETE: Delete a user by id
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrReadOnly,]


class UserMeView(generics.RetrieveUpdateDestroyAPIView):
    """
    Me View Endpoint
    - GET: Get the authenticated user's profile details
    - PATCH: Update the authenticated user's profile
    - DELETE: Delete the authenticated user's profile
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrReadOnly,]


    def get_object(self, queryset=None, **kwargs):
        """
        Get the user object of the authenticated user
        """
        return self.request.user