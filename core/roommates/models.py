import os
import uuid
import shutil
import core.settings as app_settings
from django.utils import timezone
from datetime import timedelta
from django.db import models
from django.core.files.storage import get_storage_class
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from profanity.validators import validate_is_profane
from .managers import CustomUserManager
from .validators import (
    validate_lease_length,
    validate_number_bathrooms,
    validate_number_residents,
    validate_prices
)
from .image_handlers import (
    compress_resize_image,
    upload_user_profile_image,
    upload_user_gallery_image,
    upload_listing_gallery_image
)

storage_class = get_storage_class()

class User(AbstractUser):
    """
    User model that contains the fields for authenticaton and user identifying
    information.
    """
    username = None

    first_name = models.CharField(
        _('First Name'),
        max_length=150, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('First name of user.'),
    )

    last_name = models.CharField(
        _('Last Name'),
        max_length=150, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('Last name of user.'),
    )
    
    email = models.EmailField(
        _('Email'),
        max_length=254, 
        unique=True, 
        blank=False,
        help_text=_('Email of user. Must be unique.'),
    )

    profile_picture = models.ImageField(
        _('Image'),
        upload_to=upload_user_profile_image, 
        blank=True,
        null=True, 
        default='images/users/profile/default.jpeg',
        help_text=_('Profile picture of user. If none choses default displayed.'),
    )
    
    date_of_birth = models.DateField(
        _('Date Of Birth'),
        blank=False,
        help_text=_('Date of birth of user. Must be 18 years old or older'),
    )

    about_me = models.CharField(
        _('About Me'),
        max_length=500, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('Short description about the user.'),
    )
    
    university = models.CharField(
        _('University'),
        max_length=80, 
        blank=True,
        null=True, 
        help_text=_('University that user goes to. Can be empty.'),
    )

    university_major = models.CharField(
        _('University Major'),
        max_length=50, 
        blank=True,
        null=True, 
        validators=[validate_is_profane],
        help_text=_('University major of user. Can be empty.'),
    )

    profession = models.CharField(
        _('Profession'),
        max_length=80, 
        blank=True,
        null=True, 
        validators=[validate_is_profane],
        help_text=_('Profession of user. Can be empty.'),
    )
    
    city = models.CharField(
        _('City'),
        max_length=32, 
        blank=False,
        help_text=_('Canadian city the user currently resides.'),
    )

    province = models.CharField(
        _('Province'),
        max_length=25, 
        blank=False,
        help_text=_('Canadian province the user currently resides.'),
    )

    is_lister = models.BooleanField(
        _('Is Lister'),
        default=False, 
        blank=True,
        null=True, 
        help_text=_('Specifies if user has a listing. Set when listing created.'),
    )

    created_at = models.DateTimeField(
         _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when user instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when user instance was last updated.'),
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
            'first_name', 
            'last_name', 
            'date_of_birth'
            'about_me',
            'current_city',
            'current_province',
    ]
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        """
        Saves a new user instance. Also compresses and resizes user profile
        picture.
        """
        if not self.id:
            self.profile_picture = compress_resize_image(
                self.profile_picture,
                app_settings.PROFILE_IMAGE_DIMENSION_WIDTH, 
                app_settings.PROFILE_IMAGE_DIMENSION_HEIGHT,
            )
        super(User, self).save()
    

def default_expiry_date():
    """
    Sets a default expiry on every new listing of 30 days.
    """
    now = timezone.now().date()
    return now + timedelta(days=30)


class Listing(models.Model):
    """
    Model that describes a rental listing and its required fields.
    """

    # A set of allowed room types
    UNKNOWN             = 'Unknown'
    BEDROOM             = 'Bedroom'
    SHARED_BEDROOM      = 'Shared Bedroom'
    DEN                 = 'Den'
    LIVING_ROOM         = 'Living Room'
    SHARED_LIVING_ROOM  = 'Shared Living Room'
    SUNROOM             = 'Sunroom'
    CLOSET              = 'Closet'

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
                
    poster = models.OneToOneField(
        User, 
        verbose_name=_('User'),
        on_delete=models.CASCADE, 
        help_text=_('The associated user the listing belongs to.'),
    )

    listing_title = models.CharField(
        _('Listing Title'),
        max_length=70, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('Title of the rental listing.'),
    )

    slug = models.SlugField(
        _('Slug'),
        max_length=250, 
        unique=True,
        help_text=_('Slug to generate a unique url for the listing.'),
    )

    room_desc = models.CharField(
        _('Room Description'),
        max_length=1024, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('A description of the room being listed.'),
    )

    room_type = models.CharField(
        _('Room Type'),
        max_length=18, 
        choices=ROOM_TYPES, 
        default=UNKNOWN,
        blank=False,
        help_text=_('Specifies room type from set of room choices.'),
    )

    is_furnished = models.BooleanField(
        _('Is Furnished'),
        blank=False,
        help_text=_('Indicates whether listed room is furnished.'),
    )

    is_air_conditioned = models.BooleanField(
        _('Is Air Conditioned'),
        blank=False,
        help_text=_('Indicates whether listed room has air conditioning.'),
    )

    is_laundry_ensuite = models.BooleanField(
        _('Is Laundry Ensuite'),
        blank=False,
        help_text=_('Indicates whether listed room has ensuite laundry.'),
    )

    number_of_bathrooms = models.PositiveIntegerField(
        _('Number Of Bathrooms'),
        blank=False,
        validators=[validate_number_bathrooms],
        help_text=_('Indicates number of bathrooms for rental property.'),
    )

    number_of_residents = models.PositiveIntegerField(
        _('Number Of Residents'),
        blank=False,
        validators=[validate_number_residents],
        help_text=_('Indicates number of current tenants in rental property.'),
    )

    rent_per_month = models.DecimalField(
        _('Rent Per Month'),
        max_digits=6, 
        decimal_places=2, 
        blank=False,
        validators=[validate_prices],
        help_text=_('Rent per month between $0.00 to $9,999.99.'),
    )

    extra_expenses_per_month = models.DecimalField(
        _('Extra Expenses Per Month'),
        max_digits=5, 
        decimal_places=2,
        validators=[validate_prices],
        help_text=_('Extra expenses per month between $0.00 to $999.99.'),
    )

    length_of_lease = models.PositiveIntegerField(
        _('Length of Lease'),
        blank=False,
        validators=[validate_lease_length],
        help_text=_('Specifies length of lease between 1 to 24 months.'),
    )

    address1 = models.CharField(
        _('Address 1'),
        max_length=1024, 
        blank=False,
        help_text=_('Address of rental property without unit/apt/floor number.'),
    )

    address2 = models.CharField(
        _('Address 2'),
        max_length=10, 
        blank=True,
        null=True, 
        help_text=_('Unit/apt/floor number of rental property.'),
    )

    postal_code_validator = RegexValidator(
        regex=r'^(?!.*[DFIOQU])[A-VXY][0-9][A-Z]●?[0-9][A-Z][0-9]$',
        message="Enter a postal code in the following format XXX XXX"
    )

    postal_code = models.CharField(
        _('Postal Code'),
        max_length=6,
        blank=False,
        validators=[postal_code_validator],
        help_text=_('Canadian postal code of rental property.'),
    )

    city = models.CharField(
        _('City'),
        max_length=32, 
        blank=False,
        help_text=_('Canadian city of rental property.'),
    )

    province = models.CharField(
        _('Province'),
        max_length=25, 
        blank=False,
        help_text=_('Canadian province of rental property.'),
    )

    earliest_move_in_date = models.DateField(
        _('Earliest Move In Date'),
        blank=False,
        help_text=_('Specifies earlist move in date for rental property.'),
    )

    listing_expiry_date = models.DateField(
        _('Listing Expiry Date'),
        default=default_expiry_date,
        help_text=_('Specifies expiry date of listing. Default 30 days from lisitng.'),
    )

    listing_visits = models.PositiveIntegerField(
        _('Listing Visits'),
        default=0,
        help_text=_('Specifies number of visits for this listing.'),
    )

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when listing instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when listing instance was last updated.'),
    )

    objects = models.Manager() # default manager
    listingobjects = ListingObjects() # custom manager for valid listings

    def save(self, *args, **kwargs):
        """
        Before saving model instance a custom slug url is generated for the
        listing. The slug url is made unique by appending a random 4 character
        string to the city and listing title for the listing.
        """
        if not self.slug:
            slug_str = '%s %s %s' % (
                self.city, 
                self.listing_title, 
                uuid.uuid4()
            )
            self.slug = slugify(slug_str)
        super(Listing, self).save(*args, **kwargs)

    def __str__(self):
        return self.listing_title


class Gallery(models.Model):
    """
    Model that represents a gallery for a listing or user
    """

    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        blank=True,
        null=True, 
        help_text=_('Gallery belongs to associated user.'), 
    )

    listing = models.ForeignKey(
        Listing,
        verbose_name=_('Listing'),
        on_delete=models.CASCADE,
        blank=True,
        null=True, 
        help_text=_('Gallery belongs to associated listing.'), 
    )

    uuid = models.CharField(
        _('UUID'),
        max_length=36, 
        unique=True,
        default=uuid.uuid4,
        help_text=_('Name of gallery is unique UUID. Generated on instance creation.'),
    )

    is_listing_gallery = models.BooleanField(
        _('Is Listing Gallery'),
        blank=False,
        help_text=_('Indicates if this gallery belongs to a listing.'),
    )

    is_user_gallery = models.BooleanField(
        _('Is User Gallery'),
        blank=False,
        help_text=_('Indicates if this gallery belongs to a user.'),
    )

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when gallery instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when gallery instance was last updated.'),
    )

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')
    
    def __str__(self):
        return self.uuid

    def delete_gallery(self):
        """
        Deletes all images stored in the gallery folder and then deletes the
        gallery folder itself (i.e. deletes the directory tree for the gallery).
        """

        dir_path = os.path.join(
            storage_class.location,
            self.uuid
        )

        shutil.rmtree(dir_path)


class UserImageGallery(models.Model):
    """
    Model associates a set of images to a specific user instance
    """
    user = models.ForeignKey(
        User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        help_text=_('Image belongs to associated user.'), 
    )

    image = models.ImageField(
        _('Image'), 
        upload_to=upload_user_gallery_image,
        default='images/users/gallery/default.jpeg',
        help_text=_('Image instance in filesystem'),
    )
    
    created_at = models.DateTimeField(
         _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when user image instace was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when user image instace was last updated.'),
    )

    class Meta:
        verbose_name = _('UserImageGallery')
        verbose_name_plural = _('UserImageGallerys')
    
    def __str__(self):
        return self.image.name

class ListingImageGallery(models.Model):
    """
    Model associates a set of images to a specific listing instance
    """
    listing = models.ForeignKey(
        Listing,
        verbose_name= _('Listing'),
        on_delete=models.CASCADE,
        help_text=_('Image belongs to associated listing'),
    )

    image = models.ImageField(
        _('Image'), 
        upload_to=upload_listing_gallery_image,
        default='images/listings/default.jpeg'
    )
    
    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when listing image instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when listing image instance was last updated.'),
    )
    