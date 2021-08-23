from rest_framework import serializers
from django.contrib.auth import get_user_model
from roommates.models import Listing, UserImageGallery
from cities_light.models import City, Region

User = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):
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
        Do custom validation for the city and province using the cities-light
        dataset and profile image extension
        """
        # Validate province 
        province = data['province']
        if Region.objects.filter(name__iexact=province).first() is None:
            raise serializers.ValidationError("Please enter a valid province")

        province_instance = Region.objects.filter(name__iexact=province).first()
        data['province'] = province_instance.name

        # Validate city
        city = data['city']
        if City.objects.filter(
                region_id=province_instance.id
            ).filter(
                name__iexact=city
            ).first() is None:
            raise serializers.ValidationError("Please enter a valid city")
        
        city_instance = City.objects.filter(
                region_id=province_instance.id
            ).filter(
                name__iexact=city
            ).first()
        data['city'] = city_instance.name
        return data 

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
            'profile_picture',
            'date_of_birth',
            'about_me',
            'university',
            'university_major',
            'profession',
            'city',
            'province',
            'is_lister',
            'listings',
        )
    
    def validate(self, data):
        """
        Do custom validation for the city and province using the cities-light
        dataset
        """
        # Validate province
        if data.get('province', None) is not None: 
            province = data['province']
            if Region.objects.filter(name__iexact=province).first() is None:
                raise serializers.ValidationError("Please enter a valid province")

            province_instance = Region.objects.filter(name__iexact=province).first()
            data['province'] = province_instance.name

        # Validate city
        if data.get('city', None) is not None:
            city = data['city']
            if City.objects.filter(
                    region_id=province_instance.id
                ).filter(
                    name__iexact=city
                ).first() is None:
                raise serializers.ValidationError("Please enter a valid city")
            
            city_instance = City.objects.filter(
                    region_id=province_instance.id
                ).filter(
                    name__iexact=city
                ).first()
            data['city'] = city_instance.name
        return data


class UserImageGallerySerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField())
    class Meta:
        model = UserImageGallery
        fields = (
            'user',
            'image',
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
        Do custom validation for the city and province using the cities-light
        dataset
        """
        # Validate province 
        province = data['province']
        if Region.objects.filter(name__iexact=province).first() is None:
            raise serializers.ValidationError("Please enter a valid province")

        province_instance = Region.objects.filter(name__iexact=province).first()
        data['province'] = province_instance.name

        # Validate city
        city = data['city']
        if City.objects.filter(
                region_id=province_instance.id
            ).filter(
                name__iexact=city
            ).first() is None:
            raise serializers.ValidationError("Please enter a valid city")
        
        city_instance = City.objects.filter(
                region_id=province_instance.id
            ).filter(
                name__iexact=city
            ).first()
        data['city'] = city_instance.name
        return data
    
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
    
    def validate(self, data):
        """
        Do custom validation for the city and province using the cities-light
        dataset
        """
        # Validate province
        if data.get('province', None) is not None: 
            province = data['province']
            if Region.objects.filter(name__iexact=province).first() is None:
                raise serializers.ValidationError("Please enter a valid province")

            province_instance = Region.objects.filter(name__iexact=province).first()
            data['province'] = province_instance.name

        # Validate city
        if data.get('city', None) is not None:
            city = data['city']
            if City.objects.filter(
                    region_id=province_instance.id
                ).filter(
                    name__iexact=city
                ).first() is None:
                raise serializers.ValidationError("Please enter a valid city")
            
            city_instance = City.objects.filter(
                    region_id=province_instance.id
                ).filter(
                    name__iexact=city
                ).first()
            data['city'] = city_instance.name
        return data
    
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