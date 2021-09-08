from django.core.exceptions import ValidationError

def validate_number_residents(value):
    """
    Checks to see if the number of current residents in the rental property
    is a reasonable number. Current a value between 0 and 10.
    """
    if value < 0 or value > 10:
        raise ValidationError(
            'You entered %s' % value + 'The number of current residents '
            'exceeds our allowed range of [0, 10] residents. '
            'Please contact us for support.'
        )

def validate_number_bathrooms(value):
    """
    Checks to see if the number of bathrooms in the rental property
    is a reasonable number. Currently a value between 1 and 5.
    """
    if value <= 0 or value > 5:  # Your conditions here
        raise ValidationError(
            'You entered %s' % value + 'The number of bathrooms exceeds our '
            'allowed range of [1, 5] bathrooms. Please contact our support '
            ' team for further follow up.'
        )

def validate_lease_length(value):
    """
    Checks to see if the length of the lease is a reasonable number.
    Currently a value between 1 and 24 months.
    """
    if value <= 0 or value > 24:
        raise ValidationError(
            'A lease length of %s is invalid.' % value + 'Please enter a '
            'number between 1 and 24 months'
        )

def validate_prices(value):
    """
    Checks to see if any value that should be a price was entered as a negative
    number.
    """
    if value < 0:
        raise ValidationError(
            'A positive number must be entered. You entered %s' % value
        )
        