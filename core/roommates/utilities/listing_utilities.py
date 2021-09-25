from django.utils import timezone
from datetime import timedelta


def default_expiry_date():
    """
    Sets a default expiry on every new listing of 30 days.
    """
    now = timezone.now().date()
    return now + timedelta(days=30)
    