from rest_framework import serializers
from django.contrib.auth import get_user_model
from roommates.models import GalleryImage 

User = get_user_model()


class GalleryImageSerializer(serializers.ModelSerializer):
    """
    Serializer for handling images in a gallery
    """
    class Meta:
        model = GalleryImage
        fields = (
            'image',
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
            'image_name',   
        )