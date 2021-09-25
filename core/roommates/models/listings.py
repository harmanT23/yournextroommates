import uuid
from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from profanity.validators import validate_is_profane

from ..models import User
from ..validators import (
    validate_lease_length,
    validate_number_bathrooms,
    validate_number_residents,
    validate_prices,
)
from ..utilities import default_expiry_date

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
    
    id = models.UUIDField(
        _('ID'),
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        help_text=_('Listing ID is a uuid.'),
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

    class Meta:
        verbose_name = _('Listing')
        verbose_name_plural = _('Listings')

    def __str__(self):
        return self.listing_title

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
