from rest_framework import serializers
import core.settings as app_settings
from django.contrib.auth import get_user_model
from roommates.models import Listing, Gallery, GalleryImage 
from .validators import (
    validate_city_and_province,
    validate_complete_address,
    validate_university,
    validate_poster_user
)

User = get_user_model()

class GallerySerializer(serializers.ModelSerializer):
    """
    Serializer for creation of Gallery
    """

    req_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Gallery
        fields = (
            'uuid',
            'user',
            'listing',
            'is_listing_or_user_gallery',
            'req_user',
        )
        read_only_fields = ('uuid', 'req_user')
    
    def __init__(self, *args, **kwargs):
        if hasattr(kwargs['context']['request'], 'user'):
            user = kwargs['context']['request'].user
            super(GallerySerializer, self).__init__(*args, **kwargs)
            self.fields['req_user'].default = user

    def to_representation(self, instance):
        """
        Return only the id of the user or listing for the gallery and
        not the entire object.
        """
        response = super().to_representation(instance)
        if hasattr(response, 'user'):
            response['user'] = {
                'id': instance.user.id,
            }

        if hasattr(response, 'listing'):
            response['listing'] = {
                'id': instance.listing.id,
            }
        
        return response
    
    def validate(self, data):
        """
        Validate creation of gallery.
        - Check if user exists or has listing to make gallery
        - Check if boolean set to true but no listing
        """

        if not app_settings.DEBUG:
            req_user = data['req_user']

            if data['is_listing_or_user_gallery'] == True and\
                Listing.objects.filter(
                    poster=req_user.id
                ).first() is None:
                raise serializers.ValidationError(
                    "Cannot create gallery. User does not have a listing"
                )

            if data['is_listing_or_user_gallery'] == False and\
                req_user is None:
                raise serializers.ValidationError(
                    "Cannot create gallery. "
                    "User is not authenticated or does not exist"
                )
            
        del data['req_user']
        return data


class GalleryDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for handling gallery and images within it
    """
    gallery_images = serializers.SerializerMethodField()
    class Meta:
        model = Gallery
        fields = (
            'uuid',
            'gallery_images'
        )
    
    def get_gallery_images(self, obj):
        """
        Retrieve the set of gallery images associated with gallery
        """
        gallery_image_set = obj.galleryimage_set.all()
        image_serializer = GalleryImageSerializer(gallery_image_set, many=True)
        return image_serializer.data


class GalleryImageSerializer(serializers.ModelSerializer):
    """
    Serializer for handling images in a gallery
    """
    class Meta:
        model = GalleryImage
        fields = (
            'image_url',
            'image_name'
        )

class GalleryImageUploadSerializer(serializers.ModelSerializer):
    """
    Serializer handles uploading images
    """
    class Meta:
        model = GalleryImage
        fields = (
            'gallery',
            'image',
        )

    def to_representation(self, instance):
        """
        Return only the path of the image
        """
        response = super().to_representation(instance)
        response['image'] = {
            'path': instance.image.url,
        }
            
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
        - Check validity of provided university
        - Check validity of provided city and province
        """
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
        read_only_fields = ('id', 'gallery_set')
        

class CreateListingSerializer(serializers.ModelSerializer):
    """
    Serializer handles creation of a new listing
    """
    class Meta:
        model = Listing
        fields = (
            'id',
            'poster',
            'listing_title',
            'room_type',
            'room_desc',
            'is_furnished',
            'is_air_conditioned',
            'is_laundry_ensuite',
            'number_of_residents',
            'number_of_bathrooms',
            'length_of_lease',
            'rent_per_month',
            'extra_expenses_per_month',
            'address1',
            'address2',
            'postal_code',
            'city',
            'province',
            'earliest_move_in_date',
        )
    
    def validate(self, data):
        """
        Validate creation of new listing
        - Check if request user matches that of listing user
        - Check complete address listing is valid
        """
        request = self.context.get("request")
        validate_poster_user(request, data)
        return validate_complete_address(data) 
    
    def to_representation(self, instance):
        """
        Return only id of poster when creating listing
        """
        response = super().to_representation(instance)
        response['poster'] = { 
            'id': instance.poster.id, 
        }
        return response

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer handles retrieving details of a listing
    """

    gallery_set = GalleryDetailSerializer(
        many=True,
        read_only=True,
    )
    
    class Meta:
        model = Listing
        fields = (
            'id',
            'poster',
            'slug',
            'listing_title',
            'room_type',
            'room_desc',
            'is_furnished',
            'is_air_conditioned',
            'is_laundry_ensuite',
            'number_of_bathrooms',
            'number_of_residents',
            'length_of_lease',
            'rent_per_month',
            'extra_expenses_per_month',
            'address1',
            'address2',
            'postal_code',
            'city',
            'province',
            'earliest_move_in_date',
            'listing_expiry_date',
            'listing_visits',
            'gallery_set',
            
        )
        read_only_fields = ('id', 'gallery_set')
    
    
    def to_representation(self, instance):
        """
        Return key information of the poster for a detailed listing
        """
        response = super().to_representation(instance)
        response['poster'] = {
            'id': instance.poster.id,
            'first_name': instance.poster.first_name,
            'last_name': instance.poster.last_name,
            'profession': instance.poster.profession,
            'university': instance.poster.university,
            'university_major': instance.poster.university_major,
        }
        return response

