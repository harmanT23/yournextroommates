from django.db.models.signals import post_delete
from django.dispatch import receiver
from ..models import Gallery


@receiver(post_delete, sender=Gallery)
def gallery_postdelete(sender, instance, *args, **kwargs):
    """
    Post delete signal to handle deleting directory when delete is called
    on model instance of the gallery
    """
    try:
        instance.delete_gallery()
    except Exception as e:
        raise Exception('Unable to delete gallery.', e)