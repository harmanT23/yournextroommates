from roommates.models import Listing
from django_filters import rest_framework as filters
from django.utils.translation import gettext_lazy as _


class ListingFilter(filters.FilterSet):

    province__iexact = filters.CharFilter(
        lookup_expr='iexact',
        help_text=_('All listings that match province.'),
    )

    city__iexact = filters.CharFilter(
        lookup_expr='iexact',
        help_text=_('All listings that match city.'),
    )

    rent_per_month__lte = filters.CharFilter(
        lookup_expr='lte',
        help_text=_('All listings that are less than or equal to rent per month.'),
    )

    rent_per_month__gte = filters.CharFilter(
        lookup_expr='gte',
        help_text=_('All listings that are greater than or equal to rent per month.'),
    )

    extra_expenses_per_month__lte = filters.CharFilter(
        lookup_expr='lte',
        help_text=_('All listings that are less than or equal to extra expenses per month.'),
    )

    extra_expenses_per_month__gte = filters.CharFilter(
        lookup_expr='gte',
        help_text=_('All listings that are greater than or equal to extra expenses per month.'),
    )

    earliest_move_in_date__iexact = filters.CharFilter(
        lookup_expr='iexact',
        help_text=_('All listings that match earliest move in date.'),
    )

    length_of_lease__lte = filters.CharFilter(
        lookup_expr='lte',
        help_text=_('All listings that are less than or equal to length of lease.'),
    )

    length_of_lease__gte = filters.CharFilter(
        lookup_expr='gte',
        help_text=_('All listings that are greater than or equal to length of lease.'),
    )

    room_type = filters.CharFilter(
        lookup_expr='exact',
        help_text=_('All listings that exactly match room type'),
    )

    is_furnished = filters.CharFilter(
        lookup_expr='exact',
        help_text=_('All listings that exactly match \'is furnished\''),
    )

    is_air_conditioned = filters.CharFilter(
        lookup_expr='exact',
        help_text=_('All listings that exactly match \'is_air_conditioned\''),
    )

    is_laundry_ensuite = filters.CharFilter(
        lookup_expr='exact',
        help_text=_('All listings that exactly match \'is_laundry_ensuite\''),
    )

    poster__university__iexact = filters.CharFilter(
      lookup_expr='iexact',
      help_text=_('All listings that match university'),
    )

    poster__university_major__iexact = filters.CharFilter(
      lookup_expr='iexact',
      help_text=_('All listings that match university major.'),
    )

    poster__profession__iexact = filters.CharFilter(
      lookup_expr='iexact',
      help_text=_('All listings that match profession.'),
    )

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
                                        