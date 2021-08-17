from roommates.models import Listing
from django_filters import rest_framework as filters


class ListingFilter(filters.FilterSet):

    poster__university = filters.CharFilter(lookup_expr='icontains')
    poster__university_major = filters.CharFilter(lookup_expr='icontains')
    poster__profession = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Listing
        fields = {
          'province': ['exact'],
          'city': ['exact'],
          'rent_per_month': ['lt','gt'],
          'earliest_move_in_date': ['exact', 'lte', 'gte'],
          'length_of_lease': ['exact', 'lte', 'gte'],
          'room_type': ['exact'],
          'is_furnished': ['exact']
        }
                                        