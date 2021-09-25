
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
    parser_classes = [MultiPartParser, FormParser]
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
