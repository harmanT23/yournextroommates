from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta
from .managers import CustomUserManager

def upload_user_profile_image(instance, filename):
    ext = filename.split('.')[-1]
    n_filename = f'{instance.id}.' + ext
    return f'images/users/{instance.id}/profile/{n_filename}'

class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=254, verbose_name="email address",
                              unique=True, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    date_of_birth = models.DateField(blank=False)
    about_me = models.CharField(max_length=500, blank=False)
    
    university = models.CharField(max_length=80, blank=True)
    university_major = models.CharField(max_length=50, blank=True)

    profession = models.CharField(max_length=80, blank=True)
    
    home_city = models.CharField(max_length=32, blank=True)
    home_province = models.CharField(max_length=25, blank=True)
    current_city = models.CharField(max_length=32, blank=False)
    current_province = models.CharField(max_length=25, blank=False)

    is_lister = models.BooleanField(blank=False)
    is_seeker = models.BooleanField(blank=False)

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class UserProfileImage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    profile_picture = models.ImageField(upload_to=upload_user_profile_image, 
                                        blank=True, default='default.jpeg')

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    

def upload_user_gallery_image(instance, filename):
    ext = filename.split('.')[-1]
    n_filename = f'{filename.upper()[:4]}.' + ext
    return f'images/users/{instance.user.id}/gallery/{n_filename}'


class UserImageGallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    image = models.ImageField(upload_to=upload_user_gallery_image)
    
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

def default_expiry_date():
    now = timezone.now().date()
    return now + timedelta(days=30)

class Listing(models.Model):
    # Room Types
    UNKNOWN             = 'UNKN'
    BEDROOM             = 'BDR'
    SHARED_BEDROOM      = 'SBDR'
    DEN                 = 'DEN'
    LIVING_ROOM         = 'LR'
    SHARED_LIVING_ROOM  = 'SLR'
    SUNROOM             = 'SR'
    CLOSET              = 'CLO'

    ROOM_TYPES = (
        (UNKNOWN,            'Unknown'),
        (BEDROOM,            'Bedroom'),
        (SHARED_BEDROOM,     'Shared Bedroom'),
        (DEN,                'Den'),
        (LIVING_ROOM,        'Living Room'),
        (SHARED_LIVING_ROOM, 'Shared Living Room'),
        (SUNROOM,            'Sunroom'),
        (CLOSET,             'Closet'),
    )

    class ListingObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(
                    listing_expiry_date__gt=timezone.now()
                )
                
    poster = models.OneToOneField(User, on_delete=models.CASCADE, blank=False,
                                  related_name='listings')
    
    listing_title = models.CharField(max_length=70, blank=False)

    room_type = models.CharField(max_length=4, choices=ROOM_TYPES, 
                                 default=UNKNOWN)
    room_desc = models.CharField(max_length=1024, blank=False)
    is_furnished = models.BooleanField(blank=False)
    
    number_of_residents = models.PositiveIntegerField(blank=False)
    rent_per_month = models.DecimalField(max_digits=7, decimal_places=2, 
                                         blank=False)
    extra_expenses_per_month = models.DecimalField(max_digits=6, 
                                                   decimal_places=2)

    address1 = models.CharField(max_length=1024, blank=False)
    address2 = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=6, blank=False)
    city = models.CharField(max_length=32, blank=False)
    province = models.CharField(max_length=25, blank=False)
    
    earliest_move_in_date = models.DateField(blank=False)
    listing_expiry_date = models.DateField(default=default_expiry_date)

    listing_visits = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)

    objects = models.Manager() # default manager
    listingobjects = ListingObjects() # custom manager for valid listings


def upload_listing_gallery_image(instance, filename):
    return f'images/listings/{instance.listing.id}/gallery/{filename}'


class ListingImageGallery(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, blank=False)
    image = models.ImageField(upload_to=upload_listing_gallery_image)
    
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=True)