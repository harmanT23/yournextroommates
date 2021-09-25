from django.db.models.signals import pre_save
from django.dispatch import receiver
from ..models import Listing


@receiver(pre_save, sender=Listing)
def listing_presave(sender, instance, *args, **kwargs):
    """
    Checks if a listing with the same address already exists in the database
    """

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
    ).exist()

    if is_duplicate:
      raise Exception('Listing for this address already exists')
      