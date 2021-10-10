from django.db.models import F


def update_viewcount(listing_inst):
    """
    Increments the view count for the listing by 1 using F expression
    to avoid race conditions.
    """
    listing_inst.listing_visits = F('listing_visits') + 1
    listing_inst.save()
