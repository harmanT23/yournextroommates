import difflib
import requests
from rest_framework import serializers
from cities_light.models import City, Region
import core.settings as app_settings

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


def validate_address(q_address):
    """
    Validate address uses the Google Geocode API which
    maps an address into a geographic coordinate. Returns a bool
    representing success or failure along with the formatted address.
    
    We use this API for address validation by taking
    advantage of the fact that if an address is invalid
    Google's Geocode API will return ZERO_RESULTS as the
    status code, otherwise it will return OK if no errors occurred and at 
    least one address was found. For simplicity, other possibilites such as
    OVER_QUERY_LIMIT, REQUEST_DENIED, INVALID_REQUEST, and UNKNOWN_ERROR
    are ignored and not to be expected. 
    """

    params = {
      'key': app_settings.GOOGLE_API_KEY,
      'address': q_address
    }

    response = requests.get(
      app_settings.GEOCODE_BASE_URL,
      params
    )

    json_data = response.json()

    if json_data.get('status') == 'OK':
      return (True, json_data.get('results')[0]['formatted_address'])
    else:
      return (False, '')


def validate_city_and_province(data):
    """
    Performs validation on the provided city and province. Using the 
    cities-light database.
    """

    # Validate province 
    province = data['province']
    if Region.objects.filter(name__iexact=province).first() is None:
        raise serializers.ValidationError("Please enter a valid province.")

    province_instance = Region.objects.filter(name__iexact=province).first()
    data['province'] = province_instance.name

    # Validate city
    city = data['city']
    if City.objects.filter(
            region_id=province_instance.id
        ).filter(
            name__iexact=city
        ).first() is None:
        raise serializers.ValidationError("Please enter a valid city.")
    
    city_instance = City.objects.filter(
            region_id=province_instance.id
        ).filter(
            name__iexact=city
        ).first()
    data['city'] = city_instance.name

    return data

def validate_complete_address(data):
    """
    Performs validation on a complete address using a combination of the
    cities-light database along with the Google Geocoding API. 
    Minor spelling errors or incorrect capitalization of letters 
    are corrected by the Geocoding API.
    """

    # Validate city and province
    data = validate_city_and_province(data)

    # Validate street
    query_address = data['address1'] + ', ' + data['city'] +\
        ', ' + data['province'] + ', ' + 'Canada'
    success, query_address = validate_address(query_address)
    if not success:
        raise serializers.ValidationError("Please enter a valid street.")
    data['address1'] = query_address.split(',')[0]

    return data

def validate_poster_user(request, data):
    """
    Checks if user making the request matches user used in posting
    """

    if request.user != data['poster']:
        raise serializers.ValidationError(
            "Authenticated user must match that used for listing."
        )
    
    return data
