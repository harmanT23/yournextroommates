from rest_framework import serializers
import core.settings as app_settings
from django.contrib.auth import get_user_model

from roommates.models import Listing, Gallery
from .gallery_images_serializers import  GalleryImageSerializer

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
        