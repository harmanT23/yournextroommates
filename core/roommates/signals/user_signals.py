from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from ..models import User, Gallery

@receiver(post_save, sender=User)
def create_user_gallery_postsave(sender, instance, created, *args, **kwargs):
    """
    For a newly created listing automatically create a gallery for it
    """
    if created:
        Gallery.objects.create(
            user=instance,
            is_listing_or_user_gallery=False
        )
