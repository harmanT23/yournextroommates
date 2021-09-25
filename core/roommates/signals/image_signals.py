import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ..models import GalleryImage


@receiver(post_save, sender=GalleryImage)
def gallery_image_postsave(sender, instance, created, *args, **kwargs):
    """
    For a newly created gallery image instance update the images name to the
    unique name that was chosen during creation.
    """
    if created:
        basename = os.path.basename(instance.image.name)
        filename, extension = os.path.splitext(basename)
        instance.image_name = filename
        instance.save(update_fields=['image_name'])


@receiver(post_delete, sender=GalleryImage)
def gallery_image_postdelete(sender, instance, *args, **kwargs):
    """
    Post delete signal to handle deleting image when delete is called
    on model instance of the gallery image
    """
    try:
        instance.delete_image()
    except Exception as e:
        raise Exception('Unable to delete image.', e)