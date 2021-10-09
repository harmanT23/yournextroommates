from rest_framework import serializers
from django.contrib.auth import get_user_model

from .gallery_serializers import GalleryDetailSerializer
from ..api_validators import (
    validate_city_and_province,
    validate_university,
)

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
    """
    Serializer handles registration of a new user
    """
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'profile_picture',
            'date_of_birth',
            'about_me',
            'university',
            'university_major',
            'profession',
            'city',
            'province',
        )
        extra_kwargs = {'password' : {'write_only': True}}


    def validate(self, data):
        """
        Validate creation of user profile
        - Check validity of provided university if present
        - Check validity of provided city and province
        """

        if hasattr(data, 'university'):
            data = validate_university(data)

        data = validate_city_and_province(data) 
        return data


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer handles obtaining user profile information
    """
    listings = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=True,
    )

    gallery_set = GalleryDetailSerializer(
        many=True,
        read_only=True,
    )
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'profile_picture',
            'date_of_birth',
            'about_me',
            'university',
            'university_major',
            'profession',
            'city',
            'province',
            'listings',
            'gallery_set',
        )
        read_only_fields = ('id', 'listings', 'gallery_set')
