import os
import uuid
import shutil
import core.settings as app_settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..models import (
    User,
    Listing,
)


class Gallery(models.Model):
    """
    Model that represents a gallery of images for a listing or user.
    Provides helper functions to manage gallery (i.e. delete gallery folder)
    """

    uuid = models.CharField(
        _('UUID'),
        max_length=36, 
        unique=True,
        default=uuid.uuid4,
        help_text=_('Name of gallery is its UUID. Generated on instance creation.'),
    )

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

    is_listing_or_user_gallery = models.BooleanField(
        _('Is Listing Gallery'),
        blank=False,
        help_text=_('Gallery belongs to Listing if true, else for User'),
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
        verbose_name_plural = _('Galleries')
    
    def __str__(self):
        return self.uuid

    def delete_gallery(self):
        """
        Deletes all images stored in the gallery folder and then deletes the
        gallery folder itself (i.e. deletes the directory tree for the gallery).
        """
        
        gallery_type = 'listings' if self.is_listing_or_user_gallery else 'users'
        
        dir_path = os.path.join(
            app_settings.MEDIA_ROOT,
            app_settings.GALLERY_SUBDIRECTORY,
            gallery_type,
            self.uuid
        )

        full_path = os.path.abspath(dir_path)
        
        if os.path.isdir(full_path):    
            shutil.rmtree(full_path)
