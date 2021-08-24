from roommates.models import Listing
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _


class ListingFilter(filters.FilterSet):
    class Meta:
        model = Listing
        fields = {
            'province': ['iexact'],
            'city': ['iexact'],
            'rent_per_month': ['lte','gte'],
            'extra_expenses_per_month': ['lte','gte'],
            'earliest_move_in_date': ['iexact'],
            'length_of_lease': ['lte', 'gte'],
            'room_type': ['exact'],
            'is_furnished': ['exact'],
            'is_air_conditioned': ['exact'],
            'is_laundry_ensuite': ['exact'],
            'poster__university': ['iexact'],
            'poster__university_major': ['iexact'],
            'poster__profession': ['iexact'],
        }
                                        