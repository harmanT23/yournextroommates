from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    profile_picture = models.ImageField(null=True, blank=False)
    date_of_birth = models.DateField(blank=False)
    about_me = models.CharField(max_length=500, blank=False)
    
    university = models.CharField(max_length=80)
    university_major = models.CharField(max_length=50)

    profession = models.CharField(max_length=80)
    
    home_city = models.CharField(max_length=32)
    home_province = models.CharField(max_length=25)
    current_city = models.CharField(max_length=32, blank=False)
    current_province = models.CharField(max_length=25, blank=False)

    is_lister = models.BooleanField(blank=False)
    is_seeker = models.BooleanField(blank=False)

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


def upload_user_gallery_image(instance, filename):
    return f'images/users/{instance.user.id}/gallery/{filename}'


class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    image = models.ImageField(upload_to=upload_user_gallery_image)
    
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


class RoomTypes(models.Model):
    BEDROOM             = 1
    SHARED_BEDROOM      = 2
    DEN                 = 3
    LIVING_ROOM         = 4
    SHARED_LIVING_ROOM  = 5
    SUNROOM             = 6
    CLOSET              = 7

    ROOM_TYPES = (
        (BEDROOM,            'bedroom'),
        (SHARED_BEDROOM,     'shared_bedroom'),
        (DEN,                'den'),
        (LIVING_ROOM,        'living_room'),
        (SHARED_LIVING_ROOM, 'shared_living_room'),
        (SUNROOM,            'sunroom'),
        (CLOSET,             'closet'),
    )

    id = models.PositiveSmallIntegerField(choices=ROOM_TYPES, primary_key=True)


class Listing(models.Model):
    poster = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    
    address1 = models.CharField(max_length=1024, blank=False)
    address2 = models.CharField(max_length=10, blank=False)
    postal_code = models.CharField(max_length=5, blank=False)
    city = models.CharField(max_length=32, blank=False)
    province = models.CharField(max_length=25, blank=False)

    room_type = models.ManyToManyField(RoomTypes, blank=False)
    room_desc = models.CharField(max_length=1024, blank=False)
    is_furnished = models.BooleanField(blank=False)

    number_current_residents = models.PositiveIntegerField(blank=False)
    rent_per_month = models.DecimalField(max_digits=7, decimal_places=2, 
                                         blank=False)
    additional_expenses_per_month = models.DecimalField(max_digits=6, 
                                                        decimal_places=2)
    
    earliest_move_in_date = models.DateField()
    latest_move_in_date = models.DateField(blank=False)

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


def upload_listing_gallery_image(instance, filename):
    return f'images/listings/{instance.listing.id}/gallery/{filename}'


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=False)
    image = models.ImageField(upload_to=upload_listing_gallery_image)
    
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)