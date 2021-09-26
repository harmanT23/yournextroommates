import datetime
from django.core.exceptions import ValidationError


def validate_user_age(date):
    """
    Checks to see if the user's age is >= 18 years.
    """

    if (datetime.date.today - date < datetime.timedelta(18 * 365)):
        raise ValidationError(
            'You must be at least 18 years of age to make an account'
        )
