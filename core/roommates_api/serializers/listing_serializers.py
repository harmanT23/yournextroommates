from rest_framework import serializers
from django.contrib.auth import get_user_model

from roommates.models import Listing
from .gallery_serializers import GalleryDetailSerializer
from .user_serializers import UserSerializer
from ..api_validators import validate_complete_address

User = get_user_model()


class CreateListingSerializer(serializers.ModelSerializer):
    """
    Serializer handles creation of a new listing
    """
    class Meta:
        model = Listing
        fields = (
            'id',
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
        - Check complete address listing is valid
        """
        request = self.context.get("request")
        data['poster'] = request.user

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
        read_only_fields = (
            'id', 
            'poster', 
            'slug',
            'listing_expiry_date',
            'listing_visits', 
            'gallery_set',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['gallery_set'].context.update(self.context)   


    def to_representation(self, instance):
        """
        Return key information of the poster for a detailed listing
        """
        response = super().to_representation(instance)
        user_data = UserSerializer(instance.poster, context=self.context).data
        response['poster'] = {
            'id': user_data['id'],
            'profile_picture': user_data['profile_picture'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'profession': user_data['profession'],
            'university': user_data['university'],
            'university_major': user_data['university_major'],
        }

        return response
