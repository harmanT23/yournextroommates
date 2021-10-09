import uuid
import core.settings as app_settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from profanity.validators import validate_is_profane
from ..managers import CustomUserManager

from ..utilities import (
    compress_resize_image,
    upload_user_profile_image,
)
from ..validators import validate_user_age

class User(AbstractUser):
    """
    User model that contains the fields for authenticaton and user identifying
    information.
    """
    username = None

    id = models.UUIDField(
        _('ID'),
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        help_text=_('User ID is a uuid.'),
    )

    first_name = models.CharField(
        _('First Name'),
        max_length=50, 
        blank=False,
        validators=[validate_is_profane],
        help_text=_('First name of user.'),
    )

    last_name = models.CharField(
        _('Last Name'),
        max_length=50, 
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
        validators=[validate_user_age],
        help_text=_('Date of birth of user. Must be 18 years old or older'),
    )

    about_me = models.CharField(
        _('About Me'),
        max_length=1024, 
        blank=True,
        null=True, 
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
        'date_of_birth',
        'city',
        'province',
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
        