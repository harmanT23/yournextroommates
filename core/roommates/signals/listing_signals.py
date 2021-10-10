from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from ..models import Listing, Gallery


@receiver(pre_save, sender=Listing)
def listing_presave(sender, instance, created=True, *args, **kwargs):
    """
    Checks if a listing with the same address already exists in the database
    """

    if not created:
        is_duplicate = Listing.objects.filter(
            address1=instance.address1
        ).filter(
            address2=instance.address2
        ).filter(
            postal_code=instance.postal_code
        ).filter(
            city=instance.city
        ).filter(
            province=instance.province
        ).first()

        if is_duplicate:
            raise Exception('Listing for this address already exists')


@receiver(post_save, sender=Listing)
def create_listing_gallery_postsave(sender, instance, created, *args, **kwargs):
    """
    For a newly created listing automatically create a gallery for it
    """
    if created:
        Gallery.objects.create(
            listing=instance,
            is_listing_or_user_gallery=True
        )
        