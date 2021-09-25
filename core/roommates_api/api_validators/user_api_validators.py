import difflib
import requests
from rest_framework import serializers
from core import settings as app_settings


def validate_university(data):
    """
    Validate the name of the university stated by the user and returns the 
    closest match.
    """

    params = {
        'name': data['university'],
        'country': 'Canada'
    }

    response = requests.get(
        app_settings.UNIVERSITY_DOMAIN_BASE_URL,
        params
    )

    json_data = response.json()

    if not json_data:
        raise serializers.ValidationError("Please enter a valid university.")

    # Gather each match into a list
    university_choices = []
    for item in json_data:
         university_choices.append(item.get('name'))

    closest_match = difflib.get_close_matches(
        data['university'],
        university_choices,
        n=1
    )

    if not closest_match:
        raise serializers.ValidationError("Please enter a valid university.")

    else:
        data['university'] = closest_match[0]

    return data