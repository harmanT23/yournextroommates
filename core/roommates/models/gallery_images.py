import os
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from ..models import Gallery
from ..utilities import upload_gallery_image


class GalleryImage(models.Model):
    """
    Model for an image belonging to a user or listing gallery.
    """

    id = models.UUIDField(
        _('ID'),
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False,
        help_text=_('Gallery Image ID is a uuid.'),
    )

    gallery = models.ForeignKey(
        Gallery,
        verbose_name=_('Gallery'),
        on_delete=models.CASCADE, 
        help_text=_('Image belongs to associated Gallery.'), 
    )

    image = models.ImageField(
        _('Image'),
        upload_to=upload_gallery_image, 
        help_text=_('Image file within the associated gallery'),
    )

    image_name = models.CharField(
        _('Path'),
        max_length=36,
        blank=True,
        null=True,
        unique=True,
        help_text=_('Name of image'),
    )

    @property
    def image_url(self):
        return self.image.url

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now=True, 
        editable=False,
        help_text=_('Indicates when image instance was created.'),
    )

    updated_at = models.DateTimeField(
        _('Updated At'),
        auto_now=True,
        editable=True,
        help_text=_('Indicates when image instance was last updated.'),
    )

    class Meta:
        verbose_name = _('Gallery Image')
        verbose_name_plural = _('Gallery Images')
    
    def __str__(self):
        return self.image_name

    def delete_image(self):
        """
        Deletes image from directory
        """
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        else:
            raise Exception("Could not delete image.")
