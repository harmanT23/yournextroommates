from rest_framework import serializers
from django.contrib.auth import get_user_model
from roommates.models import Listing

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                'email',
                'password', 
                'first_name', 
                'last_name',
                'date_of_birth',
                'about_me',
                'university',
                'university_major',
                'profession',
                'home_city',
                'home_province',
                'current_city',
                'current_province',
        )
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    listings = serializers.PrimaryKeyRelatedField(many=False,
                                                  read_only=True,)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'date_of_birth',
            'about_me',
            'university',
            'university_major',
            'profession',
            'home_city',
            'home_province',
            'current_city',
            'current_province',
            'is_lister',
            'is_seeker',
            'listings',
        )


class CreateListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = (
            'id',
            'poster',
            'listing_title',
            'room_type',
            'room_desc',
            'is_furnished',
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
        )
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['poster'] = { 'id': instance.poster.id, }
        return response

class ListingSerializer(serializers.ModelSerializer):
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
        )
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['poster'] = {
                                'id': instance.poster.id,
                                'first_name': instance.poster.first_name,
                                'last_name': instance.poster.last_name,
                                'profession': instance.poster.profession,
                                'university': instance.poster.university,
                                'university_major': 
                                        instance.poster.university_major,
                             }
        return response